from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from .models import PaintProduct, Category, Cart, CartItem, Order, OrderItem, UserProfile, Message, StaffPlanning
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string, get_template
from django.db import transaction # Import added for atomic operations
from .forms import ShippingAddressForm, UserRegisterForm, UserProfileForm, ContactForm, StaffPlanningForm # Import du formulaire de contact et planning
from django.http import HttpResponse, JsonResponse
from xhtml2pdf import pisa
from django.contrib.admin.views.decorators import staff_member_required # Import pour restreindre l'accès à l'admin
from django.utils import timezone
from django.db.models import Sum, Count
from collections import defaultdict # Import pour regrouper les commandes
from django.contrib.auth.models import User # Import du modèle User

# Create your views here.

# Liste des produits avec recherche et filtre
def product_list(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    gamme = request.GET.get('gamme', '')
    products = PaintProduct.objects.all()
    categories = Category.objects.all()
    
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(color__icontains=query))
    if category_id:
        products = products.filter(category_id=category_id)
    if gamme:
        products = products.filter(gamme=gamme)
        
    return render(request, 'store/product_list.html', {
        'products': products, 
        'categories': categories, 
        'query': query, 
        'category_id': category_id,
        'gamme': gamme
    })

# Détail produit
def product_detail(request, pk):
    product = get_object_or_404(PaintProduct, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

# Inscription utilisateur
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # Utilise le nouveau formulaire
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Votre compte a été créé avec succès !")
            return redirect('store:product_list')
    else:
        form = UserRegisterForm() # Utilise le nouveau formulaire
    return render(request, 'store/register.html', {'form': form})

# Connexion utilisateur
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bienvenue, {user.username} !")
            return redirect('store:product_list')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe invalide.")
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

# Déconnexion utilisateur
@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté.")
    return redirect('store:product_list')

# Ajout au panier
@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(PaintProduct, pk=pk)
    quantity = int(request.POST.get('quantity', 1)) # Récupérer la quantité depuis le formulaire

    if quantity <= 0:
        messages.error(request, "La quantité doit être supérieure à zéro.")
        return redirect('store:product_detail', pk=pk) # Rediriger vers la page de détail si erreur

    if quantity > product.stock:
        messages.error(request, f"Quantité insuffisante en stock pour {product.name}. Stock disponible: {product.stock}")
        return redirect('store:product_detail', pk=pk)

    cart, created = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    # Si l'article existe déjà dans le panier, augmenter la quantité
    if not created:
        new_quantity = item.quantity + quantity
        if new_quantity > product.stock:
            messages.warning(request, f"Vous avez déjà {item.quantity} de {product.name} dans votre panier. Le stock disponible est de {product.stock}. Votre panier a été ajusté au maximum disponible.")
            item.quantity = product.stock
        else:
            item.quantity = new_quantity
    else:
        item.quantity = quantity

    item.save()
    messages.success(request, f"{quantity} x {product.name} ajouté au panier.")
    return redirect('store:cart_detail')

# Affichage du panier
@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items_data = []
    cart_total = 0
    for item in cart.items.all():
        item_total = item.product.price * item.quantity
        cart_items_data.append({
            'item': item,
            'item_total': item_total
        })
        cart_total += item_total

    return render(request, 'store/cart_detail.html', {
        'cart': cart,
        'cart_items_data': cart_items_data,
        'cart_total': cart_total
    })

# Modifier/supprimer un article du panier
@login_required
def update_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))

        if quantity <= 0:
            item.delete()
            messages.info(request, f"{item.product.name} a été retiré du panier.")
        else:
            # Vérifier le stock disponible pour la nouvelle quantité
            if quantity > item.product.stock:
                messages.warning(request, f"Quantité insuffisante en stock pour {item.product.name}. Stock disponible: {item.product.stock}. La quantité a été ajustée.")
                item.quantity = item.product.stock
            else:
                item.quantity = quantity
            item.save()
            messages.success(request, f"Quantité de {item.product.name} mise à jour à {item.quantity}.")
    return redirect('store:cart_detail')

# Passer une commande
@login_required
def place_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.items.exists():
        messages.error(request, "Votre panier est vide et ne peut pas être commandé.")
        return redirect('store:product_list')
    
    # Re-vérifier le stock juste avant de passer la commande
    for item in cart.items.all():
        if item.quantity > item.product.stock:
            messages.error(request, f"Stock insuffisant pour {item.product.name}. Veuillez ajuster votre panier.")
            return redirect('store:cart_detail')

    if request.method == 'POST':
        shipping_form = ShippingAddressForm(request.POST)
        if shipping_form.is_valid():
            # Créez la commande avec les données du formulaire de livraison
            with transaction.atomic():
                order = Order.objects.create(
                    user=request.user,
                    total=0, # Sera mis à jour plus tard
                    shipping_address=shipping_form.cleaned_data['shipping_address'],
                    shipping_city=shipping_form.cleaned_data['shipping_city'],
                    shipping_postal_code=shipping_form.cleaned_data['shipping_postal_code'],
                    shipping_country=shipping_form.cleaned_data['shipping_country']
                )

                order.status = 'Confirmée'
                total = 0
                for item in cart.items.all():
                    OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)
                    total += item.product.price * item.quantity
                    item.product.stock -= item.quantity
                    item.product.save()
                order.total = total
                order.save()
                cart.items.all().delete()

                # Envoi de l'e-mail de confirmation
                subject = f"Confirmation de votre commande INTER PAINT #{order.id}"
                context_email = {'order': order, 'request': request}
                html_message = render_to_string('store/order_confirmation_email.html', context_email)
                from_email = 'no-reply@interpaint.com'
                to_email = request.user.email if request.user.email else 'elasrighali2003@gmail.com'

                msg = EmailMessage(subject, html_message, from_email, [to_email])
                msg.content_subtype = "html"
                try:
                    msg.send()
                    messages.success(request, "Votre commande a été confirmée et un e-mail de confirmation vous a été envoyé. Merci de votre achat !")
                except Exception as e:
                    messages.error(request, f"Votre commande a été confirmée, mais l'e-mail de confirmation n'a pas pu être envoyé. Erreur: {e}")

                return redirect('store:order_history')
        else:
            # Si le formulaire n'est pas valide, affichez la page avec les erreurs
            messages.error(request, "Veuillez corriger les erreurs dans votre adresse de livraison.")
            # Le formulaire (invalide) est déjà dans shipping_form
    else:
        # Pré-remplir le formulaire d'adresse de livraison avec les infos du profil utilisateur
        user_profile = request.user.profile
        initial_data = {
            'shipping_address': user_profile.address,
            'shipping_city': user_profile.city,
            'shipping_postal_code': user_profile.postal_code,
            'shipping_country': user_profile.country,
        }
        shipping_form = ShippingAddressForm(initial=initial_data)

    cart_items = cart.items.all()
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'shipping_form': shipping_form,
    }
    return render(request, 'store/place_order.html', context)

# Historique des commandes
@login_required
def order_history(request):
    # Exclure les commandes avec les statuts 'Expédiée', 'Livrée', ou 'Annulée'
    orders = Order.objects.filter(user=request.user).exclude(status__in=['Expédiée', 'Livrée', 'Annulée']).order_by('-created_at')
    return render(request, 'store/order_history.html', {'orders': orders})

# Formulaire de contact
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message_body = form.cleaned_data['message']
            
            # Préparer le contenu de l'email à envoyer
            email_content = f"""
            Nouveau message de contact reçu :
            
            Nom : {name}
            Email : {email}
            Sujet : {subject}
            
            Message :
            {message_body}
            
            ---
            Ce message a été envoyé depuis le formulaire de contact du site INTER PAINT.
            """
            
            # Enregistrer le message comme un ticket interne (Message model)
            # Chercher un super-utilisateur ou un staff pour être le destinataire
            recipient_user = None
            if request.user.is_authenticated and request.user.is_staff:
                recipient_user = request.user # Si l'envoyeur est staff, il peut être le destinataire initial
            else:
                recipient_user = User.objects.filter(is_superuser=True).first()
                if not recipient_user:
                    recipient_user = User.objects.filter(is_staff=True).first()

            if recipient_user:
                Message.objects.create(
                    sender=request.user if request.user.is_authenticated else None, # Si l'utilisateur est connecté, il est l'expéditeur
                    recipient=recipient_user,
                    subject=f"[CONTACT] {subject}", # Ajout d'un préfixe pour les tickets de contact
                    body=f"Nom: {name}\nEmail: {email}\n\n{message_body}"
                )
                messages.info(request, "Votre message a été enregistré en interne.")
            else:
                messages.warning(request, "Aucun administrateur ou membre du staff trouvé pour enregistrer le message en interne.")

            try:
                # Envoyer l'email à l'adresse spécifiée
                send_mail(
                    subject=subject,
                    message=email_content,
                    from_email=email, # L'email de l'expéditeur du formulaire
                    recipient_list=['elasrighali2003@gmail.com'], # L'adresse où envoyer le message
                    fail_silently=False,
                )
                messages.success(request, "Votre message a été envoyé avec succès par e-mail. Nous vous répondrons dans les plus brefs délais.")
            except Exception as e:
                messages.error(request, f"Une erreur est survenue lors de l'envoi de l'e-mail: {e}. Veuillez réessayer ou nous contacter directement par téléphone.")
                print(f"Erreur d'envoi d'email: {e}")
            
            return redirect('store:contact')
    else:
        form = ContactForm()
    
    return render(request, 'store/contact.html', {'form': form})

def home(request):
    # Récupérer les produits en vedette (les plus récents ou populaires)
    featured_products = PaintProduct.objects.all()[:6]
    
    # Récupérer les catégories pour la navigation
    categories = Category.objects.all()
    
    # Statistiques pour la page d'accueil
    total_products = PaintProduct.objects.count()
    total_categories = categories.count()
    
    # Récupérer quelques produits de chaque gamme
    luxe_products = PaintProduct.objects.filter(gamme='luxe')[:3]
    pro_products = PaintProduct.objects.filter(gamme='pro')[:3]
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
        'total_products': total_products,
        'total_categories': total_categories,
        'luxe_products': luxe_products,
        'pro_products': pro_products,
    }
    
    return render(request, 'store/home.html', context)

def about(request):
    return render(request, 'store/about.html')

# Annuler une commande
@login_required
def cancel_order(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)

    if order.status in ['Expédiée', 'Livrée', 'Annulée']:
        messages.error(request, f"La commande #{order.id} ne peut pas être annulée car son statut est '{order.status}'.")
        return redirect('store:order_history')

    try:
        with transaction.atomic():
            order.status = 'Annulée'
            order.save()

            # Remettre les produits en stock
            for item in order.items.all():
                product = item.product
                product.stock += item.quantity
                product.save()
            
            messages.success(request, f"La commande #{order.id} a été annulée avec succès. Les produits ont été remis en stock.")

    except Exception as e:
        messages.error(request, f"Une erreur est survenue lors de l'annulation de la commande #{order.id}: {e}")
    
    return redirect('store:order_history')

# Modifier l'adresse de livraison d'une commande
@login_required
def edit_shipping_address(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)

    # Vérifier si la commande peut être modifiée
    if order.status in ['Expédiée', 'Livrée', 'Annulée']:
        messages.error(request, f"L'adresse de la commande #{order.id} ne peut pas être modifiée car son statut est '{order.status}'.")
        return redirect('store:order_history')

    if request.method == 'POST':
        form = ShippingAddressForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, f"L'adresse de livraison de la commande #{order.id} a été mise à jour avec succès.")
            return redirect('store:order_history')
    else:
        form = ShippingAddressForm(instance=order)

    return render(request, 'store/edit_shipping_address.html', {'form': form, 'order': order})

# Générer un rapport PDF des commandes
@login_required
def order_report_pdf(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    context = {'orders': orders, 'request': request}
    template_path = 'store/order_report_pdf.html'
    
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rapport_commandes.pdf"'
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Nous avons rencontré des erreurs <pre>' + html + '</pre>')
    return response

# Générer un rapport PDF pour une commande spécifique
@login_required
def order_detail_pdf(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    context = {'order': order, 'request': request}
    template_path = 'store/order_detail_pdf.html'
    
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="commande_{order.id}.pdf"'
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse(f'<p>Nous avons rencontré des erreurs lors de la génération du PDF:</p><pre>{pisa_status.err}</pre>')
    return response

# Suivi détaillé d'une commande par le client
@login_required
def order_tracking(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    
    # Définir les étapes du processus de commande
    order_steps = [
        {'status': 'En attente', 'description': 'Commande reçue et en cours de traitement', 'icon': '📋'},
        {'status': 'Confirmée', 'description': 'Commande confirmée et en préparation', 'icon': '✅'},
        {'status': 'En préparation', 'description': 'Votre commande est en cours de préparation', 'icon': '📦'},
        {'status': 'Expédiée', 'description': 'Votre commande a été expédiée', 'icon': '🚚'},
        {'status': 'Livrée', 'description': 'Votre commande a été livrée', 'icon': '🎉'},
        {'status': 'Annulée', 'description': 'Commande annulée', 'icon': '❌'},
    ]
    
    # Trouver l'index de l'étape actuelle
    current_step_index = None
    for i, step in enumerate(order_steps):
        if step['status'] == order.status:
            current_step_index = i
            break
    
    context = {
        'order': order,
        'order_steps': order_steps,
        'current_step_index': current_step_index,
    }
    
    return render(request, 'store/order_tracking.html', context)

# API pour obtenir le statut d'une commande (pour le rafraîchissement temps réel)
@login_required
def get_order_status(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return JsonResponse({'status': order.status})

# Générer un rapport PDF pour l'administrateur (toutes les commandes)
@staff_member_required
def admin_order_report_pdf(request):
    orders = Order.objects.all().order_by('-created_at') # Récupère toutes les commandes
    
    # Calculer les statistiques
    total_amount = orders.aggregate(total=Sum('total'))['total'] or 0
    pending_orders = orders.filter(status='En attente').count()
    confirmed_orders = orders.filter(status='Confirmée').count()
    
    context = {
        'orders': orders, 
        'request': request,
        'now': timezone.now(),
        'total_amount': total_amount,
        'pending_orders': pending_orders,
        'confirmed_orders': confirmed_orders,
    }
    template_path = 'admin/order_report_admin_pdf.html' # Nouveau template pour l'admin
    
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rapport_commandes_admin.pdf"'
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Nous avons rencontré des erreurs lors de la génération du PDF <pre>' + html + '</pre>')
    return response

# Nouveau rapport admin : commandes triées par client
@staff_member_required
def admin_order_report_by_client_pdf(request):
    orders = Order.objects.all().order_by('user__username', '-created_at')
    
    # Regrouper les commandes par client
    orders_by_client = defaultdict(list)
    for order in orders:
        orders_by_client[order.user].append(order)
        
    context = {
        'orders_by_client': dict(orders_by_client),
        'now': timezone.now(),
        'request': request,
    }
    
    template_path = 'admin/order_report_by_client_pdf.html'
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rapport_commandes_par_client.pdf"'
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Nous avons rencontré des erreurs lors de la génération du PDF <pre>' + html + '</pre>')
    return response

# Nouvelle vue pour le rapport professionnel du site
@staff_member_required
def admin_site_report_pdf(request):
    from django.utils import timezone
    
    # Statistiques globales
    total_products = PaintProduct.objects.count()
    total_categories = Category.objects.count()
    total_users = User.objects.count()
    total_orders = Order.objects.count()
    total_revenue = Order.objects.aggregate(total=Sum('total'))['total'] or 0
    
    # Statistiques des commandes par statut
    order_status_counts = {}
    for status, _ in Order.STATUS_CHOICES:
        order_status_counts[status] = Order.objects.filter(status=status).count()
        
    # Produits les plus vendus (Top 5)
    top_selling_products = OrderItem.objects.values('product__name', 'product__color') \
                                         .annotate(total_quantity=Sum('quantity')) \
                                         .order_by('-total_quantity')[:5]
    
    context = {
        'now': timezone.now(),
        'total_products': total_products,
        'total_categories': total_categories,
        'total_users': total_users,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'order_status_counts': order_status_counts,
        'top_selling_products': top_selling_products,
    }
    
    template_path = 'admin/site_report_pdf.html'
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rapport_site_professionnel.pdf"'
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Nous avons rencontré des erreurs lors de la génération du PDF <pre>' + html + '</pre>')
    return response

# Vue pour permettre à l'utilisateur de mettre à jour son profil
@login_required
def profile_update(request):
    user_profile = request.user.profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            # Ajouter un message de succès si nécessaire
            return redirect('home') # Rediriger vers la page d'accueil
    else:
        form = UserProfileForm(instance=user_profile)
    
    context = {'form': form}
    return render(request, 'store/profile_update.html', context)

def is_superuser(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(is_superuser)
def superuser_dashboard(request):
    # Données pour le tableau de bord super-utilisateur
    total_orders = Order.objects.count()
    total_products = PaintProduct.objects.count()
    total_users = User.objects.count()
    total_revenue = Order.objects.aggregate(total=Sum('total'))['total'] or 0
    
    # Commandes récentes (peut être plus pour les superusers)
    recent_orders = Order.objects.order_by('-created_at')[:10]

    # Pour les tâches prioritaires (super-utilisateur peut voir plus)
    pending_orders = Order.objects.filter(status='En attente').count()
    low_stock_products = PaintProduct.objects.filter(stock__lt=10).count()
    unread_messages = Message.objects.filter(recipient=request.user, is_read=False).count() # Messages pour le superuser

    context = {
        'total_orders': total_orders,
        'total_products': total_products,
        'total_users': total_users,
        'total_revenue': total_revenue,
        'recent_orders': recent_orders,
        'pending_orders': pending_orders,
        'low_stock_products': low_stock_products,
        'unread_messages': unread_messages,
    }
    return render(request, 'admin/superuser_dashboard.html', context)

@staff_member_required
def admin_dashboard(request):
    # Rediriger les super-utilisateurs vers leur tableau de bord dédié
    if request.user.is_superuser:
        return redirect('store:superuser_dashboard')

    # Récupérer les commandes en attente
    pending_orders = Order.objects.filter(status='En attente').count()
    
    # Récupérer les produits en stock faible (moins de 10 unités)
    low_stock_products = PaintProduct.objects.filter(stock__lt=10).count()
    
    # Récupérer les messages non lus pour l'utilisateur staff connecté
    unread_messages = Message.objects.filter(recipient=request.user, is_read=False).count()
    
    # Statistiques pour les cartes
    total_orders = Order.objects.count()
    total_products = PaintProduct.objects.count()
    recent_orders = Order.objects.order_by('-created_at')[:5]
    
    context = {
        'pending_orders': pending_orders,
        'low_stock_products': low_stock_products,
        'unread_messages': unread_messages,
        'total_orders': total_orders,
        'total_products': total_products,
        'recent_orders': recent_orders,
    }
    
    return render(request, 'admin/admin_dashboard.html', context)

@staff_member_required
def message_list(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-created_at')
    return render(request, 'admin/message_list.html', {'messages': messages})

@staff_member_required
def mark_message_read(request, pk):
    message = get_object_or_404(Message, pk=pk, recipient=request.user)
    message.is_read = True
    message.save()
    messages.success(request, "Message marqué comme lu.")
    return redirect('store:message_list')

@staff_member_required
def low_stock_products_list(request):
    products = PaintProduct.objects.filter(stock__lt=10).order_by('name')
    return render(request, 'admin/low_stock_products_list.html', {'products': products})

@staff_member_required
def new_orders_list(request):
    orders = Order.objects.filter(status='En attente').order_by('-created_at')
    return render(request, 'admin/new_orders_list.html', {'orders': orders})

@staff_member_required
def in_preparation_orders_list(request):
    orders = Order.objects.filter(status='En préparation').order_by('-created_at')
    return render(request, 'admin/in_preparation_orders_list.html', {'orders': orders})

@staff_member_required
def tickets_dashboard(request):
    return render(request, 'admin/tickets_dashboard.html')

@staff_member_required
def stock_status(request):
    products = PaintProduct.objects.all().order_by('name')
    return render(request, 'admin/stock_status.html', {'products': products})

@staff_member_required
def reorder_products(request):
    return render(request, 'admin/reorder_products.html')

@staff_member_required
def staff_planning(request):
    if request.method == 'POST':
        form = StaffPlanningForm(request.POST)
        if form.is_valid():
            planning_entry = form.save(commit=False)
            planning_entry.staff_member = request.user
            planning_entry.save()
            messages.success(request, "Entrée de planning ajoutée avec succès !")
            return redirect('store:staff_planning')
    else:
        form = StaffPlanningForm()
    
    planning_entries = StaffPlanning.objects.filter(staff_member=request.user).order_by('date', 'start_time')
    
    context = {
        'form': form,
        'planning_entries': planning_entries,
    }
    return render(request, 'admin/staff_planning.html', context)

@staff_member_required
def send_stock_alert(request, pk):
    product = get_object_or_404(PaintProduct, pk=pk)
    
    # Trouver un super-utilisateur pour envoyer le message
    admin_user = User.objects.filter(is_superuser=True).first()

    if not admin_user:
        messages.error(request, "Aucun administrateur trouvé pour envoyer l'alerte.")
        return redirect('store:low_stock_products_list')

    subject = f"Alerte Stock Critique: {product.name} ({product.color})"
    body = (
        f"Le produit \"{product.name} ({product.color})\" a un stock critique de {product.stock} unités.\n"
        "Veuillez prendre les mesures nécessaires pour le réapprovisionnement."
    )
    
    Message.objects.create(
        sender=request.user,  # L'utilisateur staff qui envoie l'alerte
        recipient=admin_user, # L'administrateur qui reçoit l'alerte
        subject=subject,
        body=body,
    )
    messages.success(request, f"Alerte de stock envoyée pour {product.name} !")
    return redirect('store:low_stock_products_list')

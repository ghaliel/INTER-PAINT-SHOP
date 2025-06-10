from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import PaintProduct, Category, Cart, CartItem, Order, OrderItem
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.db import transaction # Import added for atomic operations
from .forms import ShippingAddressForm, UserRegisterForm # Import du nouveau formulaire

# Create your views here.

# Liste des produits avec recherche et filtre
def product_list(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    products = PaintProduct.objects.all()
    categories = Category.objects.all()
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(color__icontains=query))
    if category_id:
        products = products.filter(category_id=category_id)
    return render(request, 'store/product_list.html', {'products': products, 'categories': categories, 'query': query, 'category_id': category_id})

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
            return redirect('product_list')
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
            return redirect('product_list')
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
    return redirect('product_list')

# Ajout au panier
@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(PaintProduct, pk=pk)
    quantity = int(request.POST.get('quantity', 1)) # Récupérer la quantité depuis le formulaire

    if quantity <= 0:
        messages.error(request, "La quantité doit être supérieure à zéro.")
        return redirect('product_detail', pk=pk) # Rediriger vers la page de détail si erreur

    if quantity > product.stock:
        messages.error(request, f"Quantité insuffisante en stock pour {product.name}. Stock disponible: {product.stock}")
        return redirect('product_detail', pk=pk)

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
    return redirect('cart_detail')

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
    return redirect('cart_detail')

# Passer une commande
@login_required
def place_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.items.exists():
        messages.error(request, "Votre panier est vide et ne peut pas être commandé.")
        return redirect('product_list')
    
    # Re-vérifier le stock juste avant de passer la commande
    for item in cart.items.all():
        if item.quantity > item.product.stock:
            messages.error(request, f"Stock insuffisant pour {item.product.name}. Veuillez ajuster votre panier.")
            return redirect('cart_detail')

    # Pour l'instant, utilisez des valeurs par défaut pour l'adresse de livraison
    order = Order.objects.create(
        user=request.user,
        total=0,
        shipping_address="123 Rue de la Peinture",
        shipping_city="Peinturville",
        shipping_postal_code="12345",
        shipping_country="France"
    )

    order.status = 'Confirmée'  # Définir le statut de la commande
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
    context = {'order': order, 'request': request}
    html_message = render_to_string('store/order_confirmation_email.html', context)
    from_email = 'no-reply@interpaint.com' # Remplacez par votre adresse d'expéditeur
    to_email = request.user.email if request.user.email else 'elasrighali2003@gmail.com' # Utiliser l'email de l'utilisateur s'il existe, sinon l'email fourni

    msg = EmailMessage(subject, html_message, from_email, [to_email])
    msg.content_subtype = "html" # Maintenir à 'html' si votre template est HTML
    try:
        msg.send()
        messages.success(request, "Votre commande a été confirmée et un e-mail de confirmation vous a été envoyé. Merci de votre achat !")
    except Exception as e:
        messages.error(request, f"Votre commande a été confirmée, mais l'e-mail de confirmation n'a pas pu être envoyé. Erreur: {e}")

    return redirect('order_history')

# Historique des commandes
@login_required
def order_history(request):
    # Exclure les commandes avec les statuts 'Expédiée', 'Livrée', ou 'Annulée'
    orders = Order.objects.filter(user=request.user).exclude(status__in=['Expédiée', 'Livrée', 'Annulée']).order_by('-created_at')
    return render(request, 'store/order_history.html', {'orders': orders})

# Formulaire de contact
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        send_mail(f"Contact de {name}", message, email, ['contact@votreentreprise.com'])
        messages.success(request, "Votre message a été envoyé.")
        return redirect('product_list')
    return render(request, 'store/contact.html')

def home(request):
    return render(request, 'store/home.html')

def about(request):
    return render(request, 'store/about.html')

# Annuler une commande
@login_required
def cancel_order(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)

    if order.status in ['Expédiée', 'Livrée', 'Annulée']:
        messages.error(request, f"La commande #{order.id} ne peut pas être annulée car son statut est '{order.status}'.")
        return redirect('order_history')

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
    
    return redirect('order_history')

# Modifier l'adresse de livraison d'une commande
@login_required
def edit_shipping_address(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)

    # Vérifier si la commande peut être modifiée
    if order.status in ['Expédiée', 'Livrée', 'Annulée']:
        messages.error(request, f"L'adresse de la commande #{order.id} ne peut pas être modifiée car son statut est '{order.status}'.")
        return redirect('order_history')

    if request.method == 'POST':
        form = ShippingAddressForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, f"L'adresse de livraison de la commande #{order.id} a été mise à jour avec succès.")
            return redirect('order_history')
    else:
        form = ShippingAddressForm(instance=order)

    return render(request, 'store/edit_shipping_address.html', {'form': form, 'order': order})

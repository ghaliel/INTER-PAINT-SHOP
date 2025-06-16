from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class PaintProduct(models.Model):
    GAMME_CHOICES = [
        ('luxe', 'Gamme de Luxe'),
        ('pro', 'Gamme Pro'),
        
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    color = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    gamme = models.CharField(max_length=10, choices=GAMME_CHOICES, default='pro', verbose_name='Gamme')
    image_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    lessivage = models.BooleanField(choices=[(True, 'Oui'), (False, 'Non')], default=False, verbose_name='Lessivage')
    colissage = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='Colissage (kg)')

    def __str__(self):
        return f"{self.name} ({self.color}) - {self.get_gamme_display()}"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Panier de {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(PaintProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('En attente', 'En attente'),
        ('Confirmée', 'Confirmée'),
        ('En préparation', 'En préparation'),
        ('Expédiée', 'Expédiée'),
        ('Livrée', 'Livrée'),
        ('Annulée', 'Annulée'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='En attente')
    # Champs d'adresse de livraison
    shipping_address = models.CharField(max_length=255, blank=True, null=True)
    shipping_city = models.CharField(max_length=100, blank=True, null=True)
    shipping_postal_code = models.CharField(max_length=20, blank=True, null=True)
    shipping_country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Commande #{self.id} de {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(PaintProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Commande {self.order.id})"

    def get_total(self):
        return self.quantity * self.price

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Profil de {self.user.username}"

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', null=True, blank=True) # Peut être null si message d'un visiteur
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"De {self.sender.username if self.sender else 'Visiteur'} à {self.recipient.username}: {self.subject}"

    class Meta:
        ordering = ['-created_at']

class StaffPlanning(models.Model):
    staff_member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='planning_entries')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    task_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff_member.username} - {self.date}: {self.task_description[:50]}..."

    class Meta:
        ordering = ['date', 'start_time']
        verbose_name = "Entrée de Planning"
        verbose_name_plural = "Entrées de Planning"

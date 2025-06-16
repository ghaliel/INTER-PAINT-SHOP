from django.contrib import admin
from django.utils.html import format_html
from .models import PaintProduct, Category, Cart, CartItem, Order, OrderItem

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_count', 'description_preview')
    search_fields = ('name', 'description')
    list_per_page = 20
    
    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Nombre de produits'
    
    def description_preview(self, obj):
        return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description
    description_preview.short_description = 'Description'

class PaintProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'price', 'stock', 'category', 'gamme', 'lessivage', 'colissage', 'image_tag', 'stock_status')
    list_filter = ('category', 'gamme', 'lessivage', 'stock')
    search_fields = ('name', 'color', 'category__name', 'description')
    list_editable = ('price', 'stock')
    readonly_fields = ('image_tag',)
    fieldsets = (
        ('Informations générales', {
            'fields': ('name', 'description', 'category', 'gamme')
        }),
        ('Détails produit', {
            'fields': ('color', 'price', 'stock', 'lessivage', 'colissage')
        }),
        ('Images', {
            'fields': ('image_url', 'image', 'image_tag'),
            'classes': ('collapse',)
        }),
    )
    list_per_page = 25
    
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:60px;max-width:90px;border-radius:4px;" />', obj.image.url)
        elif obj.image_url:
            return format_html('<img src="{}" style="max-height:60px;max-width:90px;border-radius:4px;" />', obj.image_url)
        return format_html('<span style="color:#999;">Aucune image</span>')
    image_tag.short_description = 'Image'
    
    def stock_status(self, obj):
        if obj.stock == 0:
            return format_html('<span style="color:red;font-weight:bold;">Rupture</span>')
        elif obj.stock < 10:
            return format_html('<span style="color:orange;font-weight:bold;">Faible ({})</span>', obj.stock)
        else:
            return format_html('<span style="color:green;font-weight:bold;">OK ({})</span>', obj.stock)
    stock_status.short_description = 'Stock'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price', 'get_total')
    
    def get_total(self, obj):
        return f"{obj.quantity * obj.price} MAD"
    get_total.short_description = 'Total'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total', 'status', 'items_count', 'status_color')
    list_filter = ('status', 'created_at', 'user')
    search_fields = ('user__username', 'user__email', 'id')
    readonly_fields = ('created_at', 'total')
    inlines = [OrderItemInline]
    actions = ['mark_as_confirmed', 'mark_as_shipped', 'mark_as_delivered']
    list_per_page = 20
    change_list_template = 'admin/change_list.html'
    list_editable = ('status',)
    
    fieldsets = (
        ('Informations client', {
            'fields': ('user', 'created_at')
        }),
        ('Statut et montant', {
            'fields': ('status', 'total')
        }),
        ('Adresse de livraison', {
            'fields': ('shipping_address', 'shipping_city', 'shipping_postal_code', 'shipping_country'),
            'classes': ('collapse',)
        }),
    )
    
    def items_count(self, obj):
        return obj.items.count()
    items_count.short_description = 'Articles'
    
    def status_color(self, obj):
        colors = {
            'En attente': '#ffc107',
            'Confirmée': '#17a2b8',
            'En préparation': '#007bff',
            'Expédiée': '#28a745',
            'Livrée': '#6c757d',
            'Annulée': '#dc3545'
        }
        color = colors.get(obj.status, '#6c757d')
        return format_html('<span style="color:{};font-weight:bold;">{}</span>', color, obj.status)
    status_color.short_description = 'Statut'
    
    def mark_as_confirmed(self, request, queryset):
        updated = queryset.update(status='Confirmée')
        self.message_user(request, f'{updated} commande(s) marquée(s) comme confirmée(s).')
    mark_as_confirmed.short_description = "Marquer comme confirmée"
    
    def mark_as_shipped(self, request, queryset):
        updated = queryset.update(status='Expédiée')
        self.message_user(request, f'{updated} commande(s) marquée(s) comme expédiée(s).')
    mark_as_shipped.short_description = "Marquer comme expédiée"
    
    def mark_as_delivered(self, request, queryset):
        updated = queryset.update(status='Livrée')
        self.message_user(request, f'{updated} commande(s) marquée(s) comme livrée(s).')
    mark_as_delivered.short_description = "Marquer comme livrée"

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'items_count', 'cart_total')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at',)
    
    def items_count(self, obj):
        return obj.items.count()
    items_count.short_description = 'Articles'
    
    def cart_total(self, obj):
        total = sum(item.product.price * item.quantity for item in obj.items.all())
        return f"{total:.2f} MAD"
    cart_total.short_description = 'Total'

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'item_total')
    list_filter = ('product__category', 'product__gamme')
    search_fields = ('cart__user__username', 'product__name')
    
    def item_total(self, obj):
        return f"{obj.product.price * obj.quantity:.2f} MAD"
    item_total.short_description = 'Total'

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'item_total')
    list_filter = ('product__category', 'product__gamme', 'order__status')
    search_fields = ('order__user__username', 'product__name')
    readonly_fields = ('order', 'product', 'quantity', 'price')
    
    def item_total(self, obj):
        return f"{obj.quantity * obj.price:.2f} MAD"
    item_total.short_description = 'Total'

# Enregistrer les modèles avec le site admin par défaut
admin.site.register(Category, CategoryAdmin)
admin.site.register(PaintProduct, PaintProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)


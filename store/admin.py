from django.contrib import admin
from .models import PaintProduct, Category, Cart, CartItem, Order, OrderItem

class PaintProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'price', 'stock', 'category', 'image_tag')
    search_fields = ('name', 'color', 'category__name')
    list_filter = ('category',)
    readonly_fields = ('image_tag',)
    
    def image_tag(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height:60px;max-width:90px;" />'
        elif obj.image_url:
            return f'<img src="{obj.image_url}" style="max-height:60px;max-width:90px;" />'
        return ""
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0 # Ne pas afficher de champs supplémentaires vides par défaut
    readonly_fields = ('product', 'quantity', 'price') # Rendre les champs en lecture seule pour éviter les modifications directes après la commande

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total', 'status')
    list_filter = ('status', 'created_at', 'user')
    search_fields = ('user__username', 'id')
    inlines = [OrderItemInline] # Afficher les articles de la commande dans l'admin de la commande

# Register your models here.
admin.site.register(PaintProduct, PaintProductAdmin)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order, OrderAdmin) # Enregistrer Order avec OrderAdmin
admin.site.register(OrderItem)

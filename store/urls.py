from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('produit/<int:pk>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('ajouter-au-panier/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('panier/', views.cart_detail, name='cart_detail'),
    path('panier/modifier/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('commander/', views.place_order, name='place_order'),
    path('commandes/', views.order_history, name='order_history'),
    path('commandes/annuler/<int:pk>/', views.cancel_order, name='cancel_order'),
    path('commandes/modifier-adresse/<int:pk>/', views.edit_shipping_address, name='edit_shipping_address'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
] 
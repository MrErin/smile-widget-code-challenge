from django.urls import path
from products import views

urlpatterns = [
    path('api/gift-cards/', views.gift_card_list, name='gift_card_list'),
    path('api/gift-cards/<pk>/', views.gift_card_detail, name="gift_card_detail"),
    path('api/products/', views.product_list, name='product_list'),
    path('api/products/<pk>/', views.product_detail, name="product_detail"),
    path('api/product-prices/', views.product_price_list,
         name='product_price_list'),
    path('api/product-prices/<pk>/', views.product_price_detail,
         name="product_price_detail"),
]

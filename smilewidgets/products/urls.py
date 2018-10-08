# from django.urls import path
# from django.conf.urls import url
# from products import views

# urlpatterns = [
#     path('api/gift-cards/', views.gift_card_list, name='gift_card_list'),
#     path('api/gift-cards/<pk>/', views.gift_card_detail, name="gift_card_detail"),
#     path('api/products/', views.product_list, name='product_list'),
#     path('api/products/<pk>/', views.product_detail, name="product_detail"),
#     path('api/product-prices/', views.product_price_list,
#          name='product_price_list'),
#     path('api/product-prices/<pk>/', views.product_price_detail,
#          name="product_price_detail"),
#     path('api/get-price/', views.PriceRequestView, name="get_price"),
# ]


from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from products import views

router = DefaultRouter()
router.register(r'gift_cards', views.GiftCardViewSet)
router.register(r'product_price', views.ProductPriceViewSet),
router.register(r'product', views.ProductViewSet),

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^get-price/(?P<productCode>.+)&(?P<date>.+)&(?P<giftCardCode>.+)/$',
        views.PriceRequestView.as_view(), name='get-price-with-gc'),
    url(r'^get-price/(?P<productCode>.+)&(?P<date>.+)/$',
        views.PriceRequestView.as_view(), name='get-price-without-gc'),
]

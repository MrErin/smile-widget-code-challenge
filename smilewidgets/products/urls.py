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

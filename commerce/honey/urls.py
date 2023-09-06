from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('detail/', views.detail, name='detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
]

# + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
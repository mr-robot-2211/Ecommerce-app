from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(), name='Ecom-home'),   
    path('User_Profile/',profileView, name= ' profile' ),
    #path('export_data_to_excel/',export_data_to_excel)
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
]

from django.urls import path
from .views import (
    CheckoutView,
    ItemDetailView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView
)

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='item-list'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('products/<slug>/', ItemDetailView.as_view(), name='products'),  # as its a detailed view, it takes in a
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    # slug. Its to handle which object its getting
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]

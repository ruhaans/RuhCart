from django.urls import path
from . import views

urlpatterns= [
    path('place', views.place_order, name='place-order'),
    path('my-orders/', views.order_history, name='order-history'),
]
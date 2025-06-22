from django.urls import path
from . import views

urlpatterns= [
    path('dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('add_product', views.add_product, name='add_product'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('orders/', views.seller_orders, name='seller_orders'),
    

]
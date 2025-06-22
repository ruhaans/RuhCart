from django.urls import path
from store import views

urlpatterns= [
    path('', views.category_list, name= 'category_list'),
    path('category/<slug:slug>/', views.product_list, name= 'product_list'),
    path('<slug:category_slug>/<slug:product_slug>', views.product_detail, name= 'product_detail'),
    path('search/', views.search_products, name='search_products')
]
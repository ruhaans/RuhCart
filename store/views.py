from django.shortcuts import render, get_object_or_404
from store.models import Category, Product


def category_list(request):
    categories= Category.objects.all()
    return render (request, 'category_list.html', {'categories' : categories})

def product_list(request, slug):
    category= get_object_or_404(Category, slug=slug)
    products= Product.objects.filter(category=category, available=True)
    return render(request, 'product_list.html', {'category': category, 'products' : products})

def product_detail(request, category_slug, product_slug):
    category= get_object_or_404(Category, slug= category_slug)
    product = get_object_or_404(Product, slug= product_slug, category=category)

    return render(request, 'product_detail.html', {'category': category, 'product': product})
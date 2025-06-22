from django.shortcuts import render, get_object_or_404
from store.models import Category, Product
from django.core.paginator import Paginator
from django.db.models import Q


def category_list(request):
    categories= Category.objects.all()
    return render (request, 'category_list.html', {'categories' : categories})

def product_list(request, slug):
    category= get_object_or_404(Category, slug=slug)
    products= Product.objects.filter(category=category, available=True)
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product_list.html', {'category': category, 'page_obj' : page_obj})


def product_detail(request, category_slug, product_slug):
    category= get_object_or_404(Category, slug= category_slug)
    product = get_object_or_404(Product, slug= product_slug, category=category, available=True)

    return render(request, 'product_detail.html', {'category': category, 'product': product})

def search_products(request):
    query= request.GET.get('query')
    products = Product.objects.filter(
        available=True
    ).filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    ) if query else []
    paginator= Paginator (products, 6)
    page_number= request.GET.get('page')
    page_obj= paginator.get_page(page_number)
    return render(request, 'search_results.html', {'page_obj': page_obj, 'query':query})
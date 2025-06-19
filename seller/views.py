from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from store.models import Product
from .forms import ProductForm

@login_required
def seller_dashboard(request):
    if request.user.role != 'seller':
        return redirect ('category_list')
    
    products= Product.objects.filter(seller=request.user)
    return render (request, 'dashboard.html', {'products': products})


def add_product(request):
    if request.user.role != 'seller':
        return redirect('category_list')
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.seller= request.user
            product.save()

            return redirect('seller_dashboard')
    else:
        form=ProductForm()

    return render(request, 'add_product.html', {'form': form})  

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.role != 'seller' or product.seller != request.user:
        return redirect('category_list')  # or seller_dashboard

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')
    else:
        form = ProductForm(instance=product)

    return render(request, 'add_product.html', {'form': form})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.role != 'seller' or product.seller != request.user:
        return redirect('seller_dashboard')
    
    if request.method == "POST":
        product.delete()

        return redirect('seller_dashboard')

    return render (request, 'delete_product.html', {'product': product})
    
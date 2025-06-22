from django.shortcuts import render, get_object_or_404 , redirect
from store.models import Product
from django.contrib.auth.models import User
from .models import Cart, CartItem

def add_to_cart(request, product_id):
    product= get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        user=request.user
        cart, created= Cart.objects.get_or_create(user=user)
    else:
        session_key= request.session.session_key
        if not session_key:
            request.session.save()
            session_key= request.session.session_key
    
        cart, created = Cart.objects.get_or_create(session_key=session_key, user=None)

    cart_item, created= CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity +=1
    cart_item.save()

    return redirect('cart_detail')

def cart_detail (request):
    if request.user.is_authenticated:
        cart= Cart.objects.filter(user=request.user).first()

    else:
        session_key= request.session.session_key
        if not session_key:
            request.session.save()
            session_key=request.session.session_key
        cart= Cart.objects.filter(session_key=session_key).first()
    
    if cart:
        cart_items= CartItem.objects.filter(cart=cart)
    else:
        cart_items=[]
    
    for item in cart_items:
        item.subtotal = item.product.price * item.quantity
    total_price = sum(item.subtotal for item in cart_items)

    return render(request, 'cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})

def update_cart_item(request, item_id):
    item= get_object_or_404(CartItem ,id=item_id)

    if request.method== "POST":
        quantity= int(request.POST.get('quantity', 1))
        
        item.quantity = quantity
        item.save()

    return redirect('cart_detail')

def remove_cart_item(request, item_id):
    item= get_object_or_404(CartItem, id=item_id)

    item.delete()

    return redirect('cart_detail')
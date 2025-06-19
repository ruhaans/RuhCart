from django.shortcuts import render, redirect, get_object_or_404
from cart.models import Cart, CartItem
from .models import Order, OrderItem

def place_order(request):
    user= request.user

    try:
        cart= Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        return redirect('cart_detail')
    
    cart_items= CartItem.objects.filter(cart=cart)

    if not cart_items.exists():
        return redirect('cart_detail')
    
    total_price= sum(item.quantity* item.product.price for item in cart_items)

    order= Order.objects.create(
        user=user,
        shipping_address= '123 sample address',
        total_price= total_price
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity= item.quantity,
            price= item.product.price
        )

    cart.delete()

    return render(request, 'place_order.html', {
    'order': order,
    'order_items': order.orderitem_set.all()
     })

def order_history(request):
    user= request.user
    orders= Order.objects.filter(user=user).order_by('created_at')
    return render(request, 'order_history.html', {'orders': orders})
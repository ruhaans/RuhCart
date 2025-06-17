from django.db import models
from django.contrib.auth.models import User
from store.models import Product


class Cart(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key= models.CharField(max_length=100, null=True, blank=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id}"

class CartItem(models.Model):
    cart= models.ForeignKey(Cart, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)
    added_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
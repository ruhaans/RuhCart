from django.db import models
from django.conf import settings
from store.models import Product

class Order(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    shipping_address= models.TextField()
    total_price= models.DecimalField(max_digits=20, decimal_places=2)

    ORDER_STATUS= [
        ('pending','Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')
    ]

    status= models.CharField(max_length=20,choices=ORDER_STATUS, default='pending')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    product_name=product.name
    quantity= models.PositiveIntegerField()
    price= models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.product_name} x {self.quantity} (₹{self.price})"
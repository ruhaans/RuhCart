from django.db import models
from django.utils.text import slugify
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=270)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=275)
    slug = models.SlugField(unique=True)
    category= models.ForeignKey("Category", on_delete=models.PROTECT)
    image = models.ImageField()
    description = models.TextField()
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    available = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

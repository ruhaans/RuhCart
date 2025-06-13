from django.contrib import admin
from store.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields= {"slug" : ("name",)}
    list_display= ["name", "slug", "created_at",]
    search_fields= ["name",]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields= {"slug" : ("name",)}
    list_display= ["name", "category", "price", "stock", "available", "updated_at",]
    list_editable= ["price", "stock", "available",]
    list_filter= ["category", "available", "updated_at",]
    search_fields= ["name", "description"]
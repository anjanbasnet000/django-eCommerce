from django.contrib import admin

from product.models import Category, Product



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['status', 'parent']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'price']
    list_filter = ['status', 'category']
    prepopulated_fields = {'slug':('title',)}

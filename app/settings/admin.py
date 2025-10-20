from django.contrib import admin
from app.settings.models import Category, ModelProduct, ImageProduct, Product

@admin.register( Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ModelProduct)
class ModelProductAdmin(admin.ModelAdmin):
    list_display = ['name']


class ImageProductInline(admin.TabularInline):
    model = ImageProduct
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'model', 'name']
    inlines = [ImageProductInline]
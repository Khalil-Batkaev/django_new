from django.contrib import admin
from .models import Product, Client, Order


@admin.action(description='Обнулить количество товара')
def reset_qty(modeladmin, request, queryset):
    queryset.update(qty=0)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at', 'address']
    search_fields = ['name']
    search_help_text = 'Поиск по имени'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'qty', 'created_at']
    list_filter = ['name', 'price', 'qty', 'created_at']
    search_fields = ['name', 'description']
    search_help_text = 'Поиск по имени и описанию'
    actions = [reset_qty]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_amount', 'created_at']
    list_filter = ['client', 'total_amount', 'created_at']
    search_fields = ['product__name']
    search_help_text = 'Поиск по названию товара'

from django.contrib import admin
from .models import Producto, ContactData

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactData)
class ContactAdmin(admin.ModelAdmin):
    pass

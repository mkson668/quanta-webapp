from django.contrib import admin

# Register your models here.
# single dot is referencing same directory file and getting the class function Product
from .models import Product

admin.site.register(Product)
from django.contrib import admin
from .models import Category
from .models import Product

admin.site.register(Category)
admin.site.register(Product)

#@admin.register(Product)
#class ProductAdmin(admin.ModelAdmin):
    #list_display = ["name", "price", "state"]
    #list_display = ["name"]
    #list_display = ["price"]
    #search_fields = ["name"]
    #list_filter = ["price"]
    #list_per_page = 2
from django.contrib import admin
from . import models

# Register your models here.



class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','slug','brand','category','price','is_active']
    list_editable = ['slug','brand','category','price','is_active']
    search_fields = ['title']
    list_per_page = 20


class BrandAdmin(admin.ModelAdmin):
    list_display = ['title','url_title','is_active']
    list_editable = ['url_title','is_active']
    search_fields = ['title']
    list_per_page = 20


class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['product','is_active']
    list_editable = ['is_active']
    list_per_page = 20


admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.Brand,BrandAdmin)
admin.site.register(models.ProductImages,ProductImagesAdmin)
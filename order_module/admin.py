from django.contrib import admin
from . import models

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','product','count','finally_price']
    list_per_page = 20
    readonly_fields = ['user','product','count','finally_price']



admin.site.register(models.Order,OrderAdmin)
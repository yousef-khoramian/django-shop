from django.contrib import admin
from . import models

# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['user_name','email','date']
    list_per_page = 20
    search_fields = ['user_name','email']
    readonly_fields = ['user_name','email','message']

admin.site.register(models.ContactUs,ContactUsAdmin)
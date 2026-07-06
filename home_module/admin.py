from django.contrib import admin
from . import models
# Register your models here.


class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['email','phone_number','is_active']
    list_editable = ['is_active']
    list_per_page = 20
    search_fields = ['email']

admin.site.register(models.SiteBanner)
admin.site.register(models.SiteSettings,SiteSettingsAdmin)
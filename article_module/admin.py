from django.contrib import admin
from . import models

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['user','title','slug','date','is_active']
    list_editable = ['title','slug','is_active']
    list_per_page = 20
    search_fields = ['title']


class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['user','article','parent','date']
    readonly_fields = ['user','article','parent','message']
    list_per_page = 20



admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.ArticleComment,ArticleCommentAdmin)
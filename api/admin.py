from django.contrib import admin
from .models import Article

# Register your models here.

@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title','descripition')
    list_display = ('title','descripition')
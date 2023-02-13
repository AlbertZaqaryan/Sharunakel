from django.contrib import admin
from .models import Notebook, NoutCategory, TypeCategory
# Register your models here.


@admin.register(Notebook)
class AdminNotebook(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'price']


@admin.register(NoutCategory, TypeCategory)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #campos de solo lectura
    list_display = ['title', 'author', 'published', 'post_categories'] # agrega los campos para presentar la dara en el administrador
    search_fields = ['title', 'author__username', 'content'] #habilita el campo de busqueda por los campos dados
    date_hierarchy = 'published' #orden por fecha.
    ordering = ['author', 'published']
    list_filter = ['author__username', 'categories__name'] #elementos para filtrar. se recomienda que sean campos relacionados

    def post_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

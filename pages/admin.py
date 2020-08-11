from django.contrib import admin
from .models import *

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = ['title', 'order']
    search_field = ['title', 'content', 'order']

admin.site.register(Page, PageAdmin)

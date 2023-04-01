from django.contrib import admin
from .models import Category, Blog


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list = ('title', 'author', 'published', 'categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author', 'categories') #author__username


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)

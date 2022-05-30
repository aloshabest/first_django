from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_ed', 'updated_ed', 'is_published', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
from django.contrib import admin

from .models import NewModel, TagModel, NewsModel


@admin.register(NewModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['news', 'news_at']
    search_fields = ['news']
    list_filter = ['news_at']


@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_title']


@admin.register(NewsModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['news_title', 'news_author', 'news_created_at']
    search_fields = ['news_title', 'news_author']
    list_filter = ['news_created_at', 'news_author']



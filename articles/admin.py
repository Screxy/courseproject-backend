from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionMixin
from .models import Article, Comment


class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment


class ArticleAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ArticleResource
    list_display = ['article_title', 'pub_date']
    date_hierarchy = 'pub_date'
    readonly_fields = ['pub_date']


class CommentAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = CommentResource
    list_display = ['article', 'author_name', 'author', 'image']
    list_filter = ['article']
    search_fields = ["author_name"]
    fieldsets = [
        ("Статья", {"fields": ["article"]}),
        ("Пользователь", {"fields": ["author_name", 'author', 'comment_text', 'image']}),
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

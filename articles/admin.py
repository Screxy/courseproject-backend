from django.contrib import admin

from .models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_title', 'pub_date']
    date_hierarchy = 'pub_date'
    readonly_fields = ['pub_date']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['article', 'author_name']
    list_filter = ['article']
    search_fields = ["author_name"]
    fieldsets = [
        ("Статья", {"fields": ["article"]}),
        ("Пользователь", {"fields": ["author_name", 'comment_text']}),
    ]


admin.site.register(Article, ArticleAdmin)

admin.site.register(Comment, CommentAdmin)

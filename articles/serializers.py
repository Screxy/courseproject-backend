from .models import Article, Comment
from rest_framework import serializers


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'article', 'author_name', 'comment_text']


class ArticlesSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True, source='comment_set')

    class Meta:
        model = Article
        fields = ['id', 'article_title', 'article_text', 'pub_date', 'comments']

from .models import Article, Comment
from rest_framework import serializers


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'article',
            'author',
            'comment_text',
        ]

    # author = serializers.SerializerMethodField()

    def get_author(self, obj):
        user = obj.author
        return user.username


class ArticlesSerializer(serializers.ModelSerializer):
    # comments = CommentsSerializer(many=True, read_only=True, source='comment_set')

    class Meta:
        model = Article
        fields = ['id', 'article_title', 'article_text', 'pub_date']

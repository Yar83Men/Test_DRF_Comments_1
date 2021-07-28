from rest_framework import serializers
from .models import ArticleModel, CommentModel


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ('title', 'content', )


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ('email', 'name', 'text', 'parent')


class ArticleDetailSerializer(serializers.ModelSerializer):
    title = serializers.RelatedField(read_only=True)
    content = serializers.RelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = ArticleModel
        fields = ('title', 'content', 'comments', )


from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from blog.models import Post


class PostSerializer(ModelSerializer):
    author = serializers.SlugField(source='author.username', read_only=True)
    class Meta:
        model = Post
        fields = "__all__"

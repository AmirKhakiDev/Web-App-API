from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import Profile


class ProfileSerializer(ModelSerializer):
    author = serializers.SlugField(source='author.username', read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'
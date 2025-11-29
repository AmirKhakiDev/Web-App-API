from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['__all__']
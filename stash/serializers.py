from djoser.serializers import UserSerializer as BaseUserSerializer , UserCreateSerializer as BaseUserCreateSerializer 
from rest_framework import serializers
from .models import *
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', ]
class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', "email"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']

class CreateAndUpdateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class StashSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Stash
        fields = ['id', 'title', 'description', 'url', 'category', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
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
        fields = ['id', 'name',]

class CreateAndUpdateCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']

class StashSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Stash
        fields = ['id', 'title', 'description', 'url','status', 'category']

class CreateAndUpdateStashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stash
        fields = ['title', 'description', 'url', 'category']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            self.fields['category'].queryset = Category.objects.filter(user=request.user)

    def validate_category(self, value):
        user = self.context['request'].user
        if value and value.user != user:
            raise serializers.ValidationError("You can only use your own categories.")
        return value
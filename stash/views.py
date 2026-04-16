from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

# Create your views here.
class StashViewSet(ModelViewSet):
    serializer_class = StashSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST'  or self.request.method == 'PATCH':
            return CreateAndUpdateStashSerializer
        return StashSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Stash.objects.filter(user=user).select_related('category')
        return queryset
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    def get_serializer_class(self, ):
        if self.request.method == 'POST'  or self.request.method == 'PATCH':
            return CreateAndUpdateCategorySerializer
        return CategorySerializer
    def get_queryset(self):
        user = self.request.user
        queryset = Category.objects.filter(user=user)
        return queryset
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
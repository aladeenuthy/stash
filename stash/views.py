from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

# Create your views here.
class StashViewSet(ModelViewSet):
    serializer_class = StashSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Stash.objects.filter(user=user).select_related('category')
        return queryset
    
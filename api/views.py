from django.shortcuts import render
from .serializers import ServiceSerializer,CategorySerializer
from rest_framework import filters
from rest_framework import generics
from blog.models import Service
from django.contrib.auth.models import Permission
from rest_framework.permissions import IsAuthenticated
from home.models import Category

# Create your views here.
class ServiceView(generics.ListCreateAPIView):
    queyset=Service.objects.all()
    serializer_class=ServiceSerializer
    permission_classes = (IsAuthenticated,)
                
    def get_queryset(self):
        queryset=Service.objects.all()
        user = self.request.user
        return queryset.filter(user=user)

class CategoryView(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=(IsAuthenticated,)
    def get_queryset(self):
        queryset=Category.objects.all()
        return queryset
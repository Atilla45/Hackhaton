from django.shortcuts import render
from .serializers import ServiceSerializer
from rest_framework import filters
from rest_framework import generics
from blog.models import Service
from django.contrib.auth.models import Permission
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ServiceView(generics.ListCreateAPIView):
    queyset=Service.objects.all()
    serializer_class=ServiceSerializer
    permission_classes = (IsAuthenticated,)
                
    def get_queryset(self):
        queryset=Service.objects.all()
        user = self.request.user
        return queryset.filter(user=user)


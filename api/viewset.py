from rest_framework import viewsets
from django.shortcuts import render
from django.urls import reverse_lazy
from blog.models import Service
from .serializers import ServiceSerializer,CategorySerializer
# from rest_framework.permissions import IsAuthenticated


class ServiceViewset(viewsets.ModelViewSet):
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer
    # permission_classes = (IsAuthenticated,)

    
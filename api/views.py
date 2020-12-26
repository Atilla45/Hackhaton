from django.shortcuts import render
from .serializers import ServiceSerializer,CategorySerializer
from rest_framework import filters
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from blog.models import Service
from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib.auth.models import Permission
from rest_framework.permissions import IsAuthenticated
from home.models import Category
from rest_framework.response import Response
# Create your views here.
class ServiceView(generics.ListCreateAPIView):
    queyset=Service.objects.all()
    serializer_class=ServiceSerializer
    permission_classes = (IsAuthenticated,)
                
    def get_queryset(self):
        queryset=Service.objects.all()
        user = self.request.user
        return queryset.filter(user=user)




    def post(self,request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.data)

    def dispatch(self, request, *args, **kwargs):
        try:
            category_id = self.request.GET['category'] 
            skill_id=self.request.GET['skill']
            self.queryset=self.queryset.filter(skill__id=skill_id)
            self.queryset = self.queryset.filter(category__id=category_id)
        except:
            pass
        return super(ServiceView, self).dispatch(request, *args, **kwargs)



class CategoryView(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        queryset=Category.objects.all()
        return queryset
    def dispatch(self, request, *args, **kwargs):
        try:
            category_id = self.request.GET['category'] 
            self.queryset = self.queryset.filter(category__id=category_id)
        except:
            pass
        return super(CategoryView, self).dispatch(request, *args, **kwargs)
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
from rest_framework import status
from home.models import Category
# from rest_framework.parsers import MultiPartParser
from rest_framework import mixins, generics
from rest_framework.response import Response
# Create your views here.
class ServiceView(generics.ListCreateAPIView,mixins.CreateModelMixin):
    queryset=Service.objects.filter(is_published=True)
    serializer_class=ServiceSerializer
    permission_classes = (IsAuthenticated,)



    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    # def post(self, request, format=None):
    #     # to access files
    #     print(request.FILES)
    #     # to access data
    #     print(request.data) 
    #     return Response({'received data': request.data})

    # def post(self,request):
    #     serializer = ServiceSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=request.data)

    # def dispatch(self, request, *args, **kwargs):
    #     try:
    #         user=self.request.user
    #         category_id = self.request.GET['category'] 
    #         skill_id=self.request.GET['skill']
    #         self.queryset=self.queryset.filter(user=user)
    #         self.queryset=self.queryset.filter(skill__id=skill_id)
    #         self.queryset = self.queryset.filter(category__id=category_id)
    #     except:
    #         pass
    #     return super(ServiceView, self).dispatch(request, *args, **kwargs)



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
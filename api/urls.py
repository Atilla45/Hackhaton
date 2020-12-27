from django.urls import path,include
from api.views import *

urlpatterns=[
    path('service/', ServiceView.as_view(),name='service'),
    path('category/', CategoryView.as_view(),name='category')
]
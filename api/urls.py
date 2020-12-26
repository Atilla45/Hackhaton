from django.urls import path,include
from api.views import *

urlpatterns=[
    path('service/', ServiceView.as_view(),name='service')
]
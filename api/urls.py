from django.urls import path,include
from rest_framework import routers
from api.views import *
from api.viewset import ServiceViewset


router = routers.DefaultRouter()
router.register(r'service',ServiceViewset)

urlpatterns=[
    path('', include(router.urls)),
    # path('service/', ServiceView.as_view(),name='service'),
    path('category/', CategoryView.as_view(),name='category'),
]
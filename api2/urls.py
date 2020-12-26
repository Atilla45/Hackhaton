from django.urls import include, path
from rest_framework import routers
from api2.views import *

router = routers.DefaultRouter()
router.register(r'skill', SkillViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

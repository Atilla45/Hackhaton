from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('service/', views.ServiceView,name='service'),
    # path('', LoginView.as_view(template_name='login.html'),name='login'),

]
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from home.views import *

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('dashboard/', login_required(DashboardView.as_view()),name='dashboard'),

]
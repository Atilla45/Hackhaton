from django.urls import path, include
from django.contrib.auth.views import LoginView
from accounts.views import *

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    

]
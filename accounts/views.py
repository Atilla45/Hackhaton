from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView
from accounts.models import CustomUser
from accounts.forms import RegisterForm

# Create your views here.

User=CustomUser

class RegisterView(CreateView):
    template_name='register.html'
    model=User
    form_class=RegisterForm
    success_url='/'


class LogoutView(LogoutView):
    pass


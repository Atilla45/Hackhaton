from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView, LoginView
from accounts.models import CustomUser
from accounts.forms import RegisterForm,LoginForm

# Create your views here.

User=CustomUser

class RegisterView(CreateView):
    template_name='register.html'
    model=User
    form_class=RegisterForm
    success_url='/'


class LoginView(LoginView):
    template_name='login.html'
    authentication_form=LoginForm
    # success_url=reverse_lazy('home')


class LogoutView(LogoutView):
    pass


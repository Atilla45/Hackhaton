from django.shortcuts import render
from django.urls import reverse_lazy
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

    def get_success_url(self):
        try:
            next=self.request.GET['next']
            if next=='search':
                category_id= self.request.GET['category_id']
                skill_id = self.request.GET['skill_id']
                href = reverse_lazy('search')+f'?category_id={category_id}&skill={skill_id}'
            return href      
        except:
            return reverse_lazy('home')


class LogoutView(LogoutView):
    pass


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from accounts.models import CustomUser

class RegisterForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name','class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name','class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email','class':'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class':'form-control'}))
    class Meta:
        model = CustomUser
        fields = ("first_name","last_name","email","username")

class LoginForm(AuthenticationForm):
    username=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email','class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'form-control'}))
    class Meta():
        model=CustomUser
        fields='__all__'
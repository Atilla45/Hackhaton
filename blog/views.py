from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import FormMixin
from django.views.generic import *
from .models import *
from .forms import *
# Create your views here.

def ServiceView(request):
    return render(request ,'service.html')
    
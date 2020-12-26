from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from home.models import Category
from blog.models import Service


# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

    def get_context_data(self):
        context={}
        context['categories']=Category.objects.all().values()
        return context

class DashboardView(TemplateView):
    template_name='dashboard.html'  

class SearchView(ListView):
    template_name='search.html'     
    queryset=Service.objects.all()
# Create your views here.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.queryset.filter()
        context['categories']=Category.objects.all().values()
        print(context)
        return context

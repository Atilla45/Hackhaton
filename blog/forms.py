from django import forms
from blog.models import Service
from django.forms import Form, ChoiceField
from django.contrib.admin import widgets                                       
from django.contrib.admin.widgets import AdminDateWidget


class ServiceForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Designer'}))
    # skills=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Skills'}))
    is_published=forms.BooleanField()
    upload_files=forms.FileField(widget=forms.FileInput())
    admit_time=forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M:%S'], widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M:%S'))
    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        if check_something():
            self.fields['is_published'].initial  = True

    class Meta:
        model=Service
        fields=['title','description','category','skill','upload_files','is_published','admit_time']
        widgets = {
            'description':forms.Textarea(attrs={
                'placeholder': 'Describe  here...'
            }),
            
        }
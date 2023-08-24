from django import forms
from django.utils.text import slugify

from .models import Image


class Image_display(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

class Update_about_me (forms.Form):
    about_me = forms.CharField(widget=forms.Textarea)

class Update_skills (forms.Form):
    update_skills = forms.CharField(widget=forms.Textarea)

class Update_education (forms.Form):
    update_education = forms.CharField(widget=forms.Textarea)

class Update_projects (forms.Form):
    update_projects = forms.CharField(widget=forms.Textarea)


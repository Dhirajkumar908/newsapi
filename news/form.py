from django import forms
from django.forms import ModelForm, TextInput, Textarea, ImageField
from . models import *

class contectForm(ModelForm):
    class Meta:
        model=contect

        fields=["name","email","url","comment"]
        widgets={}

class postForm(ModelForm):
    class Meta:
        model=post
        fields=["title",'author','Discription', 'Detailed_post',]      
        widgets = {
            'name': TextInput(attrs={'class': 'input-name'}),
            'author':TextInput(attrs={'class': 'input-autho'}),
            'Discription':Textarea(attrs={'class': 'input-Discription'}),
            'Detailed_post':Textarea(attrs={'class': 'input-Detailed_post'}),
            
        } 
from django import forms
from django.forms import ModelForm
from . models import *

class contectForm(ModelForm):
    class Meta:
        model=contect

        fields=["name","email","url","comment"]
        widgets={}

        
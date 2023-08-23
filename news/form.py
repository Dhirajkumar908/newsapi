from django import forms
from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput
from . models import *

class contectForm(ModelForm):
    class Meta:
        model=contect

        fields=["name","email","url","comment"]
        widgets={
            'name':TextInput(attrs={'class':'C_name', 'style':'width:400px; '  }),
            'email':TextInput(attrs={'class':'C_name', 'style':'width:400px; '  }),
            'url':TextInput(attrs={'class':'C_name', 'style':'width:400px; '  }),
            'comment':TextInput(attrs={'class':'C_name', 'style':'width:400px; height:300px ',  }),
        }

class postForm(ModelForm):
    class Meta:
        model=post
        fields=["title",'author','Discription', 'Detailed_post','img']      
        widgets = {
            'title': TextInput(attrs={'class': 'input-name', 'style':'width:400px; '}),
            'author':TextInput(attrs={'class': 'input-author', 'style':'width:400px; '}),
            'Discription':Textarea(attrs={'class': 'input-Discription', 'style':'width:400px; '}),
            'Detailed_post':Textarea(attrs={'class': 'input-Detailed_post', 'style':'width:400px; '}),
            
        } 
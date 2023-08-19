from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(contect)
class contectadmin(admin.ModelAdmin):
    list_display=['name','email','comment']


@admin.register(post)
class postmodel(admin.ModelAdmin):
    list_display=['title', 'author','img']
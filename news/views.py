from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import post
import requests
from .form import *


Api_key='b370fca690b74288a1606545816ef1fb'
# Create your views here.
def home(request):
    country=request.GET.get('country')
    category=request.GET.get('category')
    if category:
        url=f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={Api_key}"
        response=requests.get(url)
        data=response.json()
        articles=data['articles']
    elif country:
        url=f"https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={Api_key}"
        response=requests.get(url)
        data=response.json()
        articles=data['articles']
    else:
        url=f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={Api_key}"
        response=requests.get(url)
        data=response.json()
        articles=data['articles']
        # print(data)
    url=f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={Api_key}"
    response=requests.get(url)
    data=response.json()
    populer=data['articles']
    print(populer)

    context={
        'data':data,
        'articles':articles,
        'populer':populer
    }
    return render(request, 'index.html', context)



def about(request):
    return render(request, 'about.html')
#function of contect form 
def contact(request):
    #rendaring the form to the template
    form=contectForm()
    #taking the request from template form
    if request.method=="POST":
        data=contectForm(request.POST)        
        if data.is_valid():
            data.save()        
    context={
        'form':form,  
    }
    return render(request, 'contact.html', context)


def News_post(request):
    posts= post.objects.all()    
    Context={
        'posts':posts
    }
    return render(request, 'post.html', Context)


def add_post(request):
    if request.method=="POST":
        form=postForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/News_post')
        else:   
            return HttpResponse("<h1>There is some Error your Post is not added</h1>")
    else:
        form=postForm()
    return render(request, 'add_post.html',{'form':form})


def show(request, title):
    print(title)
    try:
        showPost = post.objects.get(title=title)  # Assuming your model is named 'post'
        print(showPost)
    except post.DoesNotExist:
        # Handle the case where the post with the given ID doesn't exist
        raise Http404("Post does not exist")

    return render(request, 'show_post.html', {'showPost': showPost})
 











 
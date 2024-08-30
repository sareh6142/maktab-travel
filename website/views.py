from urllib import request
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from blog.models import Post
import datetime


def contact_view(request):
    return render(request,"website/Contact.html")

def about_view(request):
    return render(request,"website/about.html")

def index(request):
    return render(request,"website/index.html")

def test_view(request):
    
    posts = Post.objects.filter(published_date__lte = datetime.datetime.now() )
    context ={'posts': posts}
    return render(request,"website/test.html",context)

# Create your views here.
def test_details_view(request,pk):
    post = Post.objects.get(id = pk)
    
    context ={'posts': posts}
    return render(request,"website/test.html",context)


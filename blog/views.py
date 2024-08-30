from django.shortcuts import render,get_object_or_404
from urllib import request
from .models import Post
import datetime
from django.utils import timezone

# Create your views here.
def blog_single_view(request,pk):
    post = get_object_or_404(Post,id=pk)
    post.counted_views+=1
    post.save()
    context ={'post': post}
    return render(request,"blog/blog-single.html",context)
    


def blog_view(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()  , status=1)
    context ={'posts': posts}
    return render(request,"blog/blog-home.html",context)


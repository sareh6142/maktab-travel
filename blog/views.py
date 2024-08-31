from django.shortcuts import render,get_object_or_404
from urllib import request
from .models import Post
import datetime
from django.utils import timezone

# Create your views here.
def blog_single_view(request,pk):
    
    post = get_object_or_404(Post,id=pk)
    next_post = Post.objects.filter(id__lt=post.id , status= 1).order_by('-id').first()
    prev_post =Post.objects.filter(id__gt=post.id, status = 1).order_by('-id').last()
    
    post.counted_views+=1
    post.save()
    context ={'post': post,
               'prev':prev_post,
               'next':next_post,
               }
    return render(request,"blog/blog-single.html",context)
    


def blog_view(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()  , status=1)
    context ={'posts': posts}
    return render(request,"blog/blog-home.html",context)


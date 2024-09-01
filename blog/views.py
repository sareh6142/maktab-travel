from django.shortcuts import render,get_object_or_404
from urllib import request
from .models import Post
import datetime
from django.utils import timezone

# Create your views here.
def blog_single_view(request,pk):
    
    post = get_object_or_404(Post,id=pk)

    post_first = Post.objects.filter(published_date__lte = timezone.now() , status = 1).first()
    post_last = Post.objects.filter(published_date__lte = timezone.now() , status = 1).last()


    next_post = Post.objects.filter(published_date__lte = timezone.now()).filter( id__lt=post.id , status= 1).order_by('-id').first()
    prev_post =Post.objects.filter(published_date__lte = timezone.now()).filter( id__gt=post.id, status = 1).order_by('-id').last()
    #lowest_id = Post.objects.first().id
    #highest_id = Post.objects.last().id
    post.counted_views+=1
    post.save()
    context ={'post': post,
               'prev':prev_post,
               'next':next_post,
               'post_first':post_first,
               'post_last':post_last,
               
               }
    return render(request,"blog/blog-single.html",context)
    


def blog_view(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()  , status=1)
    context ={'posts': posts}
    return render(request,"blog/blog-home.html",context)


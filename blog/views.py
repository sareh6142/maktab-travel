from django.shortcuts import render,get_object_or_404
from urllib import request
from .models import Post
import datetime
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def blog_single_view(request,pk):
    
    post = get_object_or_404(Post, id=pk , published_date__lte = timezone.now() , status = 1)

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
    


def blog_view(request,**kwargs):
    posts = Post.objects.filter(published_date__lte = timezone.now()  , status=1)
    if kwargs.get('cat_name')!= None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    elif kwargs.get('author__username')!=None:
        posts = posts.filter(author__username = kwargs['author_username'])
    
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts =posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)


    context ={'posts': posts}
    return render(request,"blog/blog-home.html",context)

def blog_category(request,cat_name):
    posts = Post.objects.filter(published_date__lte = timezone.now(), status = 1)
    posts = posts.filter(category__name= cat_name)
    context ={'posts': posts}
    return render(request,'blog/blog-home.html',context)


def blog_search(request):
    posts= Post.objects.filter(published_date__lte = timezone.now(), status=1)
    if request.method == 'Get':
        if s:= request.Get.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

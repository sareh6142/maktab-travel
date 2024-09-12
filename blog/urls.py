from django.contrib import admin
from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    
    path('', blog_view , name='index'),
    path('<int:pk>/', blog_single_view , name ='single'),
    path('author/<str:author_username>',blog_view,name ='author'),
    path('category/<str:cat_name>',blog_view, name='category'),
    path('tag/<str:tag_name>',blog_view, name='tag'),
    path('search/',blog_search,name='search'),
 

]

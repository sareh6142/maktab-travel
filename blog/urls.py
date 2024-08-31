from django.contrib import admin
from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    
    path('', blog_view , name='index'),
    path('<int:pk>/', blog_single_view , name ='single'),
 

]

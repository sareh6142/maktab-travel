from urllib import request
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from blog.models import Post
import datetime
from .forms import NewsletterForm,ContactForm
from django.contrib import messages
from django.contrib.auth.models import User



def contact_view(request):
    if request.method == 'POST':
        updated_request = request.POST.copy()
        if updated_request.get('subject') == ' ':
            updated_request.setNUll('subject')
            #updated_request.update({'subject': " "})
        Contact_Form = ContactForm(updated_request)
        #form = Contact_Form(request.POST)
        if Contact_Form.is_valid():
            action = Contact_Form.save(commit=False)
            action.name = 'unknown'
            action.save()
            messages.add_message(request,messages.SUCCESS,'OK!')
        else:
            messages.add_message(request,messages.ERROR,'NOK!')
    form = ContactForm()
    return render(request,"website/Contact.html",{'form':form})

def about_view(request):
    return render(request,"website/about.html")

def index(request):
    print(User.objects.get(email='a@a.com'))
    return render(request,"website/index.html")


def newsletter_view(request):
    if request.method =='POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'OK!')
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request,messages.ERROR,'NOK!') 

    else:
        return HttpResponseRedirect('/')




def test_view(request):
    
    posts = Post.objects.filter(published_date__lte = datetime.datetime.now() )
    context ={'posts': posts}
    return render(request,"website/test.html",context)

# Create your views here.
def test_details_view(request,pk):
    post = Post.objects.get(id = pk)
    
    context ={'posts': posts}
    return render(request,"website/test.html",context)


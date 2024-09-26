from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from django import forms


# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request,data =request.POST)
            username = form.data['username']
            password =form.data['password']
           
            if '@' not in username:
                user = authenticate(request,username=username,password = password)
            else:
                username1= User.objects.get(email=username)
                user = authenticate(request,username=username1,password = password)

            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.info(request, 'Username or password is incorrect')
                return HttpResponseRedirect(reverse( 'accounts:login' ))
                #return redirect('login')
                #return redirect('/')
                #messages.error(request, f'Incorrect Password! Try Again')
                #return HttpResponseRedirect(reverse( 'accounts:login' ))
                #messages.add_message(request,messages.ERROR,'Invalid username or password!')
                #messages.add_message(
                #request, messages.ERROR, "Incorrect user or password"
                #)
                #return HttpResponseRedirect(reverse( 'accounts:login' ))
                #return render(request,'accounts/login.html')
                #return redirect('accounts:login.html')
                #return HttpResponse('Invalid username or Password')
                #raise forms.ValidationError("User with this email doesnot exist! Create an account instead")
                #messages.error(request, 'Invalid credentials')
                return redirect('login')

                
                    
        form= AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = UserCreationForm()
        context = {'form': form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')
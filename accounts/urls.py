from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as authViews

app_name = 'accounts'
urlpatterns = [
    
    path('login/', views.login_view , name='login'),
    path('logout/', views.logout_view , name ='logout'),
    path('signup/', views.signup_view,name ='signup'),
    
    path('reset_password/',authViews.PasswordResetView.as_view(),name= 'reset_password'),
    path('reset_password_sent/',authViews.PasswordResetDoneView.as_view(),name='reset_password_done'),
    path('reset/<uidb64>/<token>/',authViews.PasswordResetConfirmView.as_view(),name='reset_password_confirm'),
    path('reset_password_complete/',authViews.PasswordResetCompleteView.as_view(),name='reset_password_complete'),

 

]

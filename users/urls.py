"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('articles/', include('articles.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path

from django.contrib.auth import views as auth_views

from .views import account_detail,logout_user,login_user,register_user,UserUpdateView,activate,PasswordsChangeView,emailSentView




app_name="users"
urlpatterns =[


    path("detail/",account_detail,name="detail_account_view"),
    path("detail/edit/",UserUpdateView.as_view(),name="detail_account_edit_view"),
    path("detail/edit/password_change/",PasswordsChangeView.as_view(),name="password_change"),


    path("password_reset/done/",emailSentView),
    re_path('^', include('django.contrib.auth.urls')),


    path("logout_user/",logout_user,name="logout"),

    path("login_user/",login_user,name="login"),

    path("register_user/",register_user,name="register_user"),

    path("activate/<uidb64>/<token>",activate,name="activate"),



]
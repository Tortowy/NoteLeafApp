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

    #
    # path("reset_password/",auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),name="reset_password"),
    # path("reset_password_sent/",auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),name="password_reset_done"),
    # path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_form.html"),name="password_reset_confirm"),
    # path("reset_password_complete/",auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),name="password_reset_complete"),

    #
    # re_path(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    # re_path(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # re_path(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    path("password_reset/done/",emailSentView),
    re_path('^', include('django.contrib.auth.urls')),


    path("logout_user/",logout_user,name="logout"),

    path("login_user/",login_user,name="login"),

    path("register_user/",register_user,name="register_user"),

    path("activate/<uidb64>/<token>",activate,name="activate"),



]
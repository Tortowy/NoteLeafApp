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
from django.urls import path

from .views import notes_passed_by_method,NoteDetailView,NoteUpdateView,NoteCreateView




app_name="notes"
urlpatterns =[


    path('',notes_passed_by_method,name="notes_list_view"),

    path("<int:id>/detail_view/",NoteDetailView.as_view(),name="detail_note_view"),
    path("<int:id>/edit_view/",NoteUpdateView.as_view(),name="update_note_view"),
    path("create_view/",NoteCreateView.as_view(),name="create_note_view"),


]
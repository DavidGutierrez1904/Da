"""Musicgram URL Configuration"""
from django.contrib import admin
from django.urls import path
from Musicgram import views as local_views
from posts import views as posts_views
from . import views




urlpatterns = [

    path('index/', local_views.index),
    #path('inicio/', views.inicio, name= 'inicio'),
    path('posts/', posts_views.list_posts),
    path('admin', admin.site.urls),

]

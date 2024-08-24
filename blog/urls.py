'''
This module will handle the mapping for paths to functions
'''
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-aboout'),
]





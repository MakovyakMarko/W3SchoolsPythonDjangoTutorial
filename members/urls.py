# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 13:22:53 2023

@author: Marko
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main, name='main'),
    path('members/',views.members, name='members'),
    path('members/details/<slug:slug>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]
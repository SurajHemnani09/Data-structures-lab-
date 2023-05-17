"""Cloud_lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cgitb import handler
from logging import Handler
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('bubble/', bubble_view),
    path('list/', list_view),
    path('merge/', merge_view),
    path('insertion/', insertion_view),
    path('assesment/', assesment_view),
    path('array/', array_view),
    path('Login/', login_view),
    path('about/', aboutUs_view),
    path('linkedlist/', linkedlist_view),
    path('stack/', stack_view),
]
handler505 = 'core.views.error_view'
# handler404 = 'core.views.error_view'
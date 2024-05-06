"""
URL configuration for softjinn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from . import views
from main_app import views as main_app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createNewIdea', main_app_views.createNewIdea),
    path('getAllIdeas', main_app_views.getAllIdeas),
    path('login/', main_app_views.LoginUser.as_view(), name='login'),
    path('register/', main_app_views.RegisterUser.as_view(), name='register'),
    path('logout/', main_app_views.logout_user, name='logout'),
    path('', main_app_views.home, name='home')
]

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
from main_app.views import (
                            createNewIdea,
                            getAllIdeas,
                            LoginUser,
                            RegisterUser,
                            ShowIdea,
                            logout_user,
                            make_response,
                            delete_response,
                            home,
                            )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createNewIdea', createNewIdea),
    path('getAllIdeas', getAllIdeas),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('ideas/<str:id>/makeResponse', make_response),
    path('ideas/<str:id>/deleteResponse', delete_response),
    path('ideas/<str:id>', ShowIdea.as_view()),
    path('', home, name='home')
]

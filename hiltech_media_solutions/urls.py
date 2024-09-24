"""
URL configuration for hiltech_media_solutions project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# This imports your views module from the current app
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('music-studio/', views.music_studio, name='music_studio'),
    path('video-editing/', views.video_editing, name='video_editing'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('web-designing/', views.web_designing, name='web_designing'),
    path('contact/success/', views.contact_success,
         name='contact_success'),  # Success page
]

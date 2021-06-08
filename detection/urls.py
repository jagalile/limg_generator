"""limg_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    re_path(r'^$', views.detection, name='detection'),
    re_path(r'^create_detection/$', views.createDetection, name='create_detection'),
    re_path(r'^create_detection_label/$', views.createDetectionLabel, name='create_detection_label'),
    re_path(r'^next_image/$', views.nextImage, name='next_image'),
    #re_path(r'^upload_images/$', views.uploadImages, name='upload_images'),
    re_path(r'^reload_form_detection/$', views.reload_form_detection, name='reload_form_detection'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
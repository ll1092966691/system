"""ScientificSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from fileHandle import views
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
import fileHandle
import os
from django.views.decorators.clickjacking import xframe_options_sameorigin

urlpatterns = [
    path('admin/', admin.site.urls),
        path('fileHandle/login/', fileHandle.views.login),
    path('fileHandle/register/', fileHandle.views.register),
    path('fileHandle/getfile/', fileHandle.views.getfile),
    path('fileHandle/deletefile/', fileHandle.views.deleteFile),
    path('fileHandle/addfile/', fileHandle.views.addFile),

    path('fileHandle/test/', fileHandle.views.test),
    path('fileHandle/uploadFile/', fileHandle.views.uploadFile),
    path('fileHandle/filemarge/', fileHandle.views.upload_and_marge),
    url(r'media/(?P<path>.*)/$', serve, {'document_root': settings.MEDIA_ROOT}),

    url(r'file/(?P<path>.*)/$', serve, {'document_root': os.path.join(settings.BASE_DIR, 'file')})
]

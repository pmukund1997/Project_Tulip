"""tulip URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views   # to provide a way to obtain token
from tulip_api_app import urls as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/',views.obtain_auth_token),  # returns token when provided username and password as formdata
    path('api/',include(api_urls))  # urls for tulip_api_app
]
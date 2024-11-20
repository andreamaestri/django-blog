"""
URL configuration for codestar project.

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
from django.urls import path, include
from filebrowser.sites import site

urlpatterns = [
    path('admin/filebrowser/', site.urls),  # filebrowser URLS
    path('admin/', admin.site.urls),  # Django admin URLs
    path("", include("blog.urls"), name="blog"),  # Blog URLs
    path('about/', include('about.urls'), name="about-urls"),  # About URLs
    path("accounts/", include("allauth.urls")),
    path('tinymce/', include('tinymce.urls')),  # TinyMCE URLs
]

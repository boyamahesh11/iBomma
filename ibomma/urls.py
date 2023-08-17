"""
URL configuration for ibomma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from app.views import *
urlpatterns = [
    path("admin/", admin.site.urls),
    path('Home/',Home.as_view(),name='Home'),
    path('Tamil/',Tamil.as_view(),name='Tamil'),
    path('Hindi/',Hindi.as_view(),name='Hindi'),
    path('About/',About.as_view(),name='About'),
    path('Bug/',Bug.as_view(),name='Bug'),
    path('Enter_Page/',Enter_Page.as_view(),name='Enter_Page'),
    path('Login/',Login, name='Login'),
    path('registration/',registration,name='registration'),
    path('Change_pas/',Change_pas,name='Change_pas'),
    path('reset_password/',reset_password,name='reset_password'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 
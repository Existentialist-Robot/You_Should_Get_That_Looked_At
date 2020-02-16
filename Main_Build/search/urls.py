"""Main_Build URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from . import views

app_name = 'search'

urlpatterns = [
    path('home/', views.upload_list, name='home'),
    path('team/', views.people_list, name='team'),
    path('mission/', views.mission, name='Mission'),
    path('contact/', views.contact, name='Contact'),
    path('upload/', views.upload, name='upload'),
    path('upload_view/<slug>/', views.upload_detail, name='upload_detail'),
    path('people/<slug>/', views.people_detail, name='people_detail'),
    # path('personal_posts/<slug>/', views.personal_upload, name='personal_upload'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.upload_list, name='upload_list_by_tag'),
    url(r'^search/(?P<search_slug>[-\w]+)/$', views.upload_search, name='upload_list_by_search'),
    path('admin/', admin.site.urls),
]

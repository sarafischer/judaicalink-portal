"""labs URL Configuration

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
from django.contrib.admin import AdminSite
from django.urls import include, path
from backend.admin import admin_site
from django.shortcuts import render

def index(request):
    #return HttpResponse(Dataset.objects.all())
    return render(request, "search/root.html")

admin.autodiscover()

urlpatterns = [
    path('admin/', admin_site.urls),
    path('backend/', include('backend.urls', namespace='backend')),
    path('search/', include('search.urls')),
    path('lod/', include('lodjango.urls')),
    path('', index, name='index'),
    path('cm_search/', include('cm_search.urls')),
]

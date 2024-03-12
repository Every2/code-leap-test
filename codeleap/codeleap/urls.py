"""
URL configuration for codeleap project.

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
from django.urls import include, path
from rest_framework import routers
from teste.api import viewset
from django.http import HttpResponseRedirect


def redirect_to_careers(request):
    return HttpResponseRedirect('/careers/')

route = routers.SimpleRouter()

route.register(r'careers', viewset.DataStructureViewSet, basename="careers")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', redirect_to_careers), # To remove bug with swagger doesn't redirect to /careers when initialized
    path('', include(route.urls)),
]

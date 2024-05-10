"""
URL configuration for myProject project.

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
from rest_framework.urlpatterns import format_suffix_patterns
from myapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('age-list/', views.agelist, name='age-list'),
    path('monthly-list/', views.monthlylist, name='monthly-list'),
    path('policest-list/', views.PoliceStlist, name='policest-list'),
    path('yearly-list/', views.yearlylist, name='yearly-list'),
    path('unidentifiedDeadBodies-list/', views.unidentifiedBodiesList, name='unidentifiedDeadBodies-list'),
    

]

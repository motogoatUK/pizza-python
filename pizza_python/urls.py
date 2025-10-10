"""
URL configuration for pizza_python project.

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),    # for signup page
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('pizza.urls'), name='pizza-urls'),
]

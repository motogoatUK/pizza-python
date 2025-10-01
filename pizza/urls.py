from django.urls import path
from . import views


urlpatterns = [
    path('', views.PizzaList.as_view(), name='home'),
]

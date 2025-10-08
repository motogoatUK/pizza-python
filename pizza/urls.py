from django.urls import path
from . import views


urlpatterns = [
    path('', views.PizzaList.as_view(), name='home'),
    path('edit/<slug:slug>', views.pizza_order, name='pizza_order'),
    path('all-pizzas/', views.MyPizzas.as_view(), name='all_pizzas'),
    path('new-pizza/', views.new_pizza, name='new_pizza'),
    path('delete-pizza/<slug:slug>/', views.delete_pizza, name='delete_pizza'),
]

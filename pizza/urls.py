from django.urls import path
from . import views


urlpatterns = [
    path('', views.PizzaList.as_view(), name='home'),
    path('edit/<slug:slug>', views.edit_pizza, name='edit_pizza'),
    path('all-pizzas/', views.MyPizzas.as_view(), name='all_pizzas'),
    path('new-pizza/', views.new_pizza, name='new_pizza'),
    path('delete-pizza/<slug:slug>/', views.delete_pizza, name='delete_pizza'),
    path('order-pizza/<slug:slug>/', views.order_pizza),
]

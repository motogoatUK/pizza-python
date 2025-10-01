from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
A single instance of Pizza related to base, toppings and user_id.
We don't usually need to create the auto-incrementing id field as Django adds
this automatically, but in this instance we want to call it order_id
"""


class Pizza(models.Model):
    order_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    cheese = models.BooleanField(default=True)
    tom_sauce = models.BooleanField(default=True, verbose_name="tomato sauce")
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="pizza_orders"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

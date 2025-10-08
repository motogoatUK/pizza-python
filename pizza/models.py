from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Pizza(models.Model):
    """
    A single instance of Pizza related to base, topping(s) and user_id.
    We don't usually need to create the auto-incrementing id field as Django
    adds this automatically, but in this instance we want to call it order_id
    """
    order_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    cheese = models.BooleanField(default=True)
    tom_sauce = models.BooleanField(default=True, verbose_name="tomato sauce")
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    # A Pizza must have one, and only one, base
    base_id = models.ForeignKey(
        'Base',
        on_delete=models.CASCADE,
        related_name='bases',
        null=False,
        blank=False
    )
    featured_image = CloudinaryField('image', default='placeholder')
    # Toppings are optional. Many Pizzas can have many Toppings
    topping_id = models.ManyToManyField(
        'Topping',
        blank=True,
        related_name='toppings'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    show_on_homepage = models.BooleanField(default=False)

    def __str__(self):
        return f"Pizza: {self.title} | created by {self.user_id}"


class Base(models.Model):
    '''
    A single instance of Base, related to Pizza
    There can be only 1 Base in a Pizza but there must be one.
    There can be many Pizzas with the same Base
    '''
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    '''
    A single instance of Topping, related to Pizza
    '''
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

from django.contrib import admin
from .models import Pizza


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'show_on_homepage')
    list_filter = ('show_on_homepage',)
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
# admin.site.register(Pizza)

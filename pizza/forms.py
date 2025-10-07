from django import forms
from .models import Pizza, Topping


class OrderForm(forms.ModelForm):
    topping_id = forms.ModelMultipleChoiceField(
            queryset=Topping.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False,
            label="Toppings:"
        )
    # featured_image = 'placeholder'

    class Meta:
        model = Pizza
        exclude = [
            'show_on_homepage',
            'slug',
            'user_id',
            'featured_image'
        ]
        labels = {
            'base_id': 'Base',
        }

from django import forms
from .models import Pizza, Topping


class OrderForm(forms.ModelForm):
    """
    form:`OrderForm`

    Allows users to add new pizzas.
    Also used to for editing existing pizzas
    Excludes admin-only fields.
    *Converts from selection field to checkboxes for ease of use*
    """
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
            'user_id',
            'featured_image',
            'num_order',
        ]
        labels = {
            'base_id': 'Base',
        }
        # Hide the slug field from the user.
        # It needs to be included in the form
        # so we can access it from javascript
        # when adding a new Pizza entry
        widgets = {
            'slug': forms.HiddenInput(),
        }

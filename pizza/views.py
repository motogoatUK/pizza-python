from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
from .models import Pizza
from .forms import OrderForm


# Create your views here.
# def index(request):
#     return HttpResponse("Hello, Pizza!")


class PizzaList(generic.ListView):
    queryset = Pizza.objects.filter(show_on_homepage=True)
    template_name = "pizza/index.html"


class MyPizzas(generic.ListView):
    queryset = Pizza.objects.all().order_by('user_id')
    template_name = "pizza/all-pizzas.html"


def new_pizza(request):
    """
    Shows blank :model:`Pizza` form.

    Once saved shows pizza list screen
    """
    if request.method == "POST":
        new_pizza = OrderForm(request.POST)
        if new_pizza.is_valid():
            # We need to add user and a slug
            new_order = new_pizza.save(commit=False)
            new_order.user_id = request.user
            new_order.slug = slugify(new_order.title)
            new_order.save()
            new_pizza.save_m2m()  # Required to save Toppings
            return HttpResponseRedirect(
                reverse('all_pizzas')+'#'+new_order.slug)
        return render(
            request,
            "pizza/new-pizza.html",
            {
                "order_form": new_pizza,
            }
        )
    else:
        order_form = OrderForm()
        return render(
            request,
            "pizza/new-pizza.html",
            {
                "order_form": order_form,
            }
        )


def edit_pizza(request, slug):
    """
    View detail of :model:`Pizza`+`Base`+`Toppings`.
    Handles POST data to save in DB

    **Context**
    ``Pizza``
        An instance of :model:`Pizza`,
    ``order_form``
        A form to update any fields.

    **Template:**
    :template:`pizza/edit-pizza.html`
    """
    queryset = Pizza.objects.all()
    order = get_object_or_404(queryset, slug=slug)
    order_form = OrderForm(instance=order)

    if request.method == "POST":
        order_form = OrderForm(data=request.POST, instance=order)
        if order_form.is_valid():
            new_order = order_form.save(commit=False)
            new_order.user_id = request.user
            # Reset slug in case of title change
            new_order.slug = slugify(new_order.title)
            new_order.save()
            order_form.save_m2m()  # Required to save Toppings
            return HttpResponseRedirect(
                reverse('all_pizzas')+'#'+new_order.slug)
        else:
            print("invalid form")

    return render(
        request,
        "pizza/edit-pizza.html",
        {
            "pizza": order,
            "order_form": order_form,
        }
    )


def delete_pizza(request, slug):
    """
    function to delete a pizza
    """
    queryset = Pizza.objects.all()
    doomed_pizza = get_object_or_404(queryset, slug=slug)
    # Check the user is the creator of the Pizza
    if doomed_pizza.user_id == request.user:
        doomed_pizza.delete()
        print('Pizza deleted!')
    else:
        print('You can only delete your own pizzas!')

    return HttpResponseRedirect(reverse('all_pizzas',))

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Pizza
from .forms import OrderForm


# Create your views here.
# def index(request):
#     return HttpResponse("Hello, Pizza!")


class PizzaList(generic.ListView):
    queryset = Pizza.objects.filter(show_on_homepage=True)
    template_name = "pizza/index.html"


class MyPizzas(generic.ListView):
    queryset = Pizza.objects.all()
    template_name = "pizza/all-pizzas.html"


def pizza_order(request, slug):
    """
    Display detail of :models: Pizza+Base+Toppings.
    **Context**
    ``Pizza``
        An instance of :model:`Pizza`.
    **Template:**
    :template:`pizza/pizza_order.html`
    """
    queryset = Pizza.objects.all()
    order = get_object_or_404(queryset, slug=slug)

    if request.method == "POST":
        order_form = OrderForm(data=request.POST, instance=order)
        if order_form.is_valid():
            new_order = order_form.save(commit=False)
            new_order.user_id = request.user
            new_order.save()
        else:
            print("invalid form")

    order_form = OrderForm(instance=order)
    return render(
        request,
        "pizza/pizza_order.html",
        {
            "pizza": order,
            "order_form": order_form,
        }
    )

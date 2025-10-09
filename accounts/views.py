from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(SuccessMessageMixin, CreateView):
    """ Django view to register a user

    *uses `SuccessMessageMixin` to output 
    success to the message system*
    """
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    success_message = "Your account has been created successfully!"\
        " You can now log in."

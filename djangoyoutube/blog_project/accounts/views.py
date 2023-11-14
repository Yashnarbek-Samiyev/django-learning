from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # reverse_lazy() is a lazily evaluated version of reverse(), used here because we're providing a URL to a class-based view attribute.
    template_name = 'signup.html'
from django.views.generic import ListView
from .models import Post, About, Contact

# Create your views here.


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'


class AboutPageView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'all__about_posts_list'


class ContactPageView(ListView):
    model = Contact
    template_name = 'contact.html'
    context_object_name = 'all_contact_posts_list'

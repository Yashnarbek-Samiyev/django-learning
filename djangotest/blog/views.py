from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from blog.models import Post
from blog.models import AboutPage
from blog.models import About
from blog.models import ContactInfo
from django.template import loader
from django.http import HttpResponse


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()[:5]
        context["About"] = About.objects.first()
        context["about"] = About.objects.first()
        context["Post"] = Post.objects.first()

        return context


def aboutpage(request):
    aboutpage = AboutPage.objects.all()
    context = {"aboutpage": aboutpage}
    return render(request, "about.html", context)


def contactinfo(request):
    contactinfo = ContactInfo.objects.all()
    context = {"contactinfo": contactinfo}
    return render(request, "contact.html", context)


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()[:5]
        context["About"] = About.objects.first()
        context["about"] = About.objects.first()
        context["Post"] = Post.objects.first()

        return context

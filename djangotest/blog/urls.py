from django.contrib import admin
from django.urls import path
from blog.views import IndexView
from blog.views import AboutView
app_name = "blog"
urlpatterns = [
    path("", IndexView.as_view()),
    path("about/", AboutView.as_view(), name="about"),
]

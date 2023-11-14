from django.shortcuts import render
from .serializers import AuthorSerializer, AuthorPostsSerializer, CategoriesSerializer, TodaysUpdateSerializer,  InstagramPostsSerializer, ConatctUsSerializer, WeAreFeaturedOnSerializer, FAQSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Author, AuthorPosts, Categories, TodaysUpdate, InstagramPosts, WeAreFeaturedOn, ContactUs, FAQ

# Create your views here.


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorPostsListView(generics.ListAPIView):
    queryset = AuthorPosts.objects.all()
    serializer_class = AuthorPostsSerializer


class CategoriesListView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class TodaysUpdateListView(generics.ListAPIView):
    queryset = TodaysUpdate.objects.all()
    serializer_class = TodaysUpdateSerializer


class InstagramPostsListView(generics.ListAPIView):
    queryset = InstagramPosts.objects.all()
    serializer_class = InstagramPostsSerializer


class WeAreFeaturedOnListView(generics.ListAPIView):
    queryset = WeAreFeaturedOn.objects.all()
    serializer_class = WeAreFeaturedOnSerializer


class ContactUsListView(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ConatctUsSerializer


class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

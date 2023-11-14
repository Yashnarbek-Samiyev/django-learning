from django.shortcuts import render

# Create your views here.
from .serializers import CategorySerializer, FeaturedArticlesSerializer, CssArticlesSerializer, JsArticlesSerializer, ReactJsArticlesSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Category, FeaturedArticles, CssAricles, JsArticles, ReactJsArticles


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FeaturedArticlesListView(generics.ListAPIView):
    queryset = FeaturedArticles.objects.all()
    serializer_class = FeaturedArticlesSerializer


class CssArticlesListView(generics.ListAPIView):
    queryset = CssAricles.objects.all()
    serializer_class = CssArticlesSerializer


class CategoriesListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class JsArticlesListView(generics.ListAPIView):
    queryset = JsArticles.objects.all()
    serializer_class = JsArticlesSerializer


class ReactJsArticlesListView(generics.ListAPIView):
    queryset = ReactJsArticles.objects.all()
    serializer_class = ReactJsArticlesSerializer

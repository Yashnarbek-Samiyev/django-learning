from django.urls import path, include
from .views import CategoryListView, FeaturedArticlesListView, CssArticlesListView, JsArticlesListView, ReactJsArticlesListView

urlpatterns = [
    path("category/", CategoryListView.as_view()),
    path("featured-articles/", FeaturedArticlesListView.as_view()),
    path("css-articles/", CssArticlesListView.as_view()),
    path("js-articles/", JsArticlesListView.as_view()),
    path("reactjs-articles/", ReactJsArticlesListView.as_view()),
]

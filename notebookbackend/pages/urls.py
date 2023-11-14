from django.urls import path, include
from .views import AuthorListView, AuthorPostsListView, CategoriesListView, TodaysUpdateListView, InstagramPostsListView, WeAreFeaturedOnListView, ContactUsListView, FAQListView


urlpatterns = [
    path('author/', AuthorListView.as_view()),
    path('categories/', CategoriesListView.as_view()),
    path('author-posts/', AuthorPostsListView.as_view()),
    path('todays-update/', TodaysUpdateListView.as_view()),
    path('instagram-posts/', InstagramPostsListView.as_view()),
    path('we-are-featured-on/', WeAreFeaturedOnListView.as_view()),
    path('contact-us/', ContactUsListView.as_view()),
    path('faq/', FAQListView.as_view()),

]

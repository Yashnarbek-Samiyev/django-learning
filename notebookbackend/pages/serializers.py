from rest_framework import serializers
from .models import Author, AuthorPosts, Categories, TodaysUpdate, InstagramPosts, WeAreFeaturedOn, ContactUs, FAQ


class AuthorSerializer(serializers.Serializer):
    class Meta:
        model = Author
        fields = "__all__"


class AuthorPostsSerializer(serializers.Serializer):
    class Meta:
        model = AuthorPosts
        fields = "__all__"


class CategoriesSerializer(serializers.Serializer):
    class Meta:
        model = Categories
        fields = "__all__"


class TodaysUpdateSerializer(serializers.Serializer):
    class Meta:
        model = TodaysUpdate
        fields = "__all__"


class InstagramPostsSerializer(serializers.Serializer):
    class Meta:
        model = InstagramPosts
        fields = "__all__"


class WeAreFeaturedOnSerializer(serializers.Serializer):
    class Meta:
        model = WeAreFeaturedOn
        fields = "__all__"


class ConatctUsSerializer(serializers.Serializer):
    class Meta:
        model = ContactUs
        fields = "__all__"


class FAQSerializer(serializers.Serializer):
    class Meta:
        model = FAQ
        fields = "__all__"

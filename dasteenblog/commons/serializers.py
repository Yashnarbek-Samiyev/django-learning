from rest_framework import serializers
from .models import Author, Category, FeaturedArticles, CssAricles, JsArticles, ReactJsArticles


class Author(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class FeaturedArticlesSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = FeaturedArticles
        fields = "__all__"


class CssArticlesSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = CssAricles
        fields = "__all__"


class JsArticlesSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = JsArticles
        fields = "__all__"


class ReactJsArticlesSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = ReactJsArticles
        fields = "__all__"

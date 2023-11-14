from django.contrib import admin
from django.apps import apps
from .models import Post, Category

admin.site.register(Post)
admin.site.register(Category)


models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

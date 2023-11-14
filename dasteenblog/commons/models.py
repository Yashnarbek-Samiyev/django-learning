from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to='images/')
    description = models.TextField()
    date = models.DateTimeField()
    time = models.DateTimeField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.FileField(upload_to='images/')

    def __str__(self):
        return self.name


class FeaturedArticles(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.FileField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CssAricles(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.FileField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class JsArticles(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.FileField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ReactJsArticles(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.FileField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    image = models.FileField(upload_to='images/')
    bio = models.TextField(max_length=100)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    pinterest_url = models.URLField(blank=True)

    top_author = models.BooleanField(default=False)
    meet_our_authors = models.BooleanField(default=False)
    author_blogs = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AuthorPosts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.FileField(upload_to='images/')
    updated_at = models.DateTimeField()
    url = models.URLField(blank=True)

    website = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    pinterest_url = models.URLField(blank=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=100)
    count = models.FloatField()
    url = models.URLField(blank=True)
    search_with_tags = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TodaysUpdate(models.Model):
    title = models.CharField(max_length=100)
    count = models.FloatField()
    url = models.URLField(blank=True)

    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class InstagramPosts(models.Model):
    image = models.FileField(upload_to='images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.url


class WeAreFeaturedOn(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    content = models.TextField()
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    pinterest_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)

    subscribe_email_news = models.EmailField(blank=True)

    blogs = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FAQ(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question

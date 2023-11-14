# Generated by Django 4.2.7 on 2023-11-14 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.FileField(upload_to='images/')),
                ('bio', models.TextField(max_length=100)),
                ('facebook_url', models.URLField(blank=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('instagram_url', models.URLField(blank=True)),
                ('pinterest_url', models.URLField(blank=True)),
                ('top_author', models.BooleanField(default=False)),
                ('meet_our_authors', models.BooleanField(default=False)),
                ('author_blogs', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('count', models.FloatField()),
                ('url', models.URLField(blank=True)),
                ('search_with_tags', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('question', models.CharField(max_length=100)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='InstagramPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeAreFeaturedOn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodaysUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('count', models.FloatField()),
                ('url', models.URLField(blank=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.categories')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('content', models.TextField()),
                ('twitter_url', models.URLField(blank=True)),
                ('instagram_url', models.URLField(blank=True)),
                ('pinterest_url', models.URLField(blank=True)),
                ('facebook_url', models.URLField(blank=True)),
                ('subscribe_email_news', models.EmailField(blank=True, max_length=254)),
                ('blogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.categories')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.FileField(upload_to='images/')),
                ('updated_at', models.DateTimeField()),
                ('url', models.URLField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('facebook_url', models.URLField(blank=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('instagram_url', models.URLField(blank=True)),
                ('pinterest_url', models.URLField(blank=True)),
                ('is_popular', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.author')),
            ],
        ),
    ]

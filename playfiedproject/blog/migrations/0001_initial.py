# Generated by Django 3.0.5 on 2020-07-10 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TagCloud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('content', models.TextField(null=True)),
                ('date', models.DateField(auto_now=True, null=True)),
                ('reply', models.ManyToManyField(to='blog.CommentReply')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=250)),
                ('post_content', models.TextField()),
                ('post_pub_date', models.DateField()),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
                ('post_comments', models.ManyToManyField(to='blog.Comment')),
                ('post_tags', models.ManyToManyField(to='blog.TagCloud')),
            ],
            options={
                'ordering': ['-post_pub_date'],
            },
        ),
    ]
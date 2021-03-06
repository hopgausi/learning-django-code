# Generated by Django 2.0.7 on 2020-07-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200710_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='post_comments',
            field=models.ManyToManyField(blank=True, to='blog.Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=models.ManyToManyField(blank=True, to='blog.CommentReply'),
        ),
        migrations.AlterField(
            model_name='commentreply',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='commentreply',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

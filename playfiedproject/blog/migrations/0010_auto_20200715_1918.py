# Generated by Django 2.0.7 on 2020-07-15 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='post_img',
            field=models.ImageField(null=True, upload_to='blog/post_pics'),
        ),
    ]

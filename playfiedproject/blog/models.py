from django.db import models
from django.conf import settings

class Category(models.Model):
    cat_name = models.CharField(max_length=50, unique=True, )

    def __str__(self):
        return self.cat_name
    

class TagCloud(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class CommentReply(models.Model):
    name = models.CharField(max_length=100)
    content =models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    reply = models.ManyToManyField(CommentReply,blank=True)
    

    def __str__(self):
        return self.name


class Article(models.Model):
    post_title = models.CharField(max_length=250)
    post_content = models.TextField()
    post_pub_date = models.DateField(auto_now=True)
    post_img = models.ImageField(upload_to='blog/post_pics', null=True)
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_tags = models.ManyToManyField(TagCloud)
    post_comments = models.ManyToManyField(Comment,blank=True)
    

    class Meta:
        ordering = ['-post_pub_date']

    def __str__(self):
        return f'{self.post_title}'

class Message(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=250, null=True)
    message = models.TextField(null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.subject
    




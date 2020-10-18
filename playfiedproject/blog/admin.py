from django.contrib import admin
from .models import (
    Article, 
    Category, 
    TagCloud,
    CommentReply,
    Comment,
    Message,
    )


admin.site.site_header = 'DJ XBlog Adminstration'
admin.site.site_title = 'DJ XBlog Adminstration Site'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_pub_date','post_author')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject','email', 'date')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(TagCloud)
admin.site.register(Comment)
admin.site.register(CommentReply)
admin.site.register(Message, MessageAdmin)




from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.db.models import Q
from django.contrib import messages
from .models import Article, Category, Comment, TagCloud
from .forms import CommentForm, MessageForm



def home(request):
    queryset = Article.objects.all()[:5]
    queryset_cat = list(set(Category.objects.all()))
    queryset_tags = list(set(TagCloud.objects.all()))
    context = {
        'object_list': queryset,
        'cat_list': queryset_cat,
        'tag_list': queryset_tags,
        'object':{
            'title': 'Welcome'
            },
    }
    template_name = 'blog/index.html' 
    return render(request,template_name, context)


def about(request):
    context = {
        'object':{
            'title': 'About'
            },
    }
    template_name = 'blog/about.html'
    return render(request, template_name, context)


def post_detail(request, id):
    object = get_object_or_404(Article, id=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save()
        object.post_comments.add(comment)
        return redirect('blog:blog-post_detail', object.id)
    context = {
        'object': object,
        'title': True,
        'form':form,
    }
    template_name = 'blog/post-detail.html'
    return render(request, template_name, context)


class BlogListView(ListView):
    model = Article
    template_name = 'blog/blog.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['cat_list'] = Category.objects.all()
        context['tag_list'] = list(set(TagCloud.objects.all()))
        context['object'] = {'title':'All Blog Posts'}
        return context
    
    
def contact(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Message sent successfully!')
        return redirect('blog:blog-home')
    context = {
        'object':{
            'title': 'Contact Us'
            },
        'form': form,
    }
    template_name = 'blog/contact.html'
    return render(request, template_name, context)

def tag_blog_list(request, tag):
    queryset_tag = TagCloud.objects.get(Q(name=tag.capitalize())|Q(name=tag.lower())|Q(name=tag.upper()))
    queryset = Article.objects.filter(post_tags=queryset_tag)
    context = {
        'object_list': queryset,
        'cat_list': list(set(Category.objects.all())),
        'tag_list': list(set(TagCloud.objects.all())),
        'tag_x': tag,
        'object':{
            'title': f'{tag.capitalize()} Tags'
            },
    }

    template_name = 'blog/blog.html'
    return render(request, template_name, context)


def category_blog_list(request, cat):
    queryset_cat = Category.objects.get(Q(cat_name=cat.capitalize())|Q(cat_name=cat.lower())|Q(cat_name=cat.upper()))
    queryset = Article.objects.filter(post_category=queryset_cat)
    context = {
        'object_list': queryset,
        'cat_list': list(set(Category.objects.all())),
        'tag_list': list(set(TagCloud.objects.all())),
        'cat_x':cat,
        'object':{
            'title': f'{cat.capitalize()} Category'
            },
    }

    template_name = 'blog/blog.html'
    return render(request, template_name, context)

# def messages(request):
#     form = MessageForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect()
#     template_name = 'blog/contact.html'


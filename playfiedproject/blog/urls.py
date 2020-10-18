from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:id>/', views.post_detail, name='blog-post_detail'),
    path('blogs/all/', views.BlogListView.as_view(), name='blog-blog_list'),
    path('blogs/tag/<str:tag>/all/', views.tag_blog_list, name='tag_blog_list'),
    path('blogs/category/<str:cat>/all/', views.category_blog_list, name='cat_blog_list'),
    path('contact/', views.contact, name='blog-contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


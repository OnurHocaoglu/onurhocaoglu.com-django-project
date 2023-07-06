from django.urls import path
from blog.views import blog_index,category_view,blog_search,blog_detail


app_name = 'blog'

urlpatterns = [
    path("",blog_index,name="blog_index"),
    path("search",blog_search,name="search"),
    path("<slug:category_slug>/",category_view,name="category_view"),
    path("<slug:category_slug>/<slug:post_slug>/",blog_detail,name="blog_detail")
]


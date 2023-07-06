from django.shortcuts import redirect, render,get_object_or_404
from django.core.paginator import Paginator

# My Models
from .models import BlogPost,BlogCategory,BlogTag


# Create your views here.

def blog_index(request):
    all_post = BlogPost.objects.filter(is_active=True).order_by('-created_at')
    categories = BlogCategory.objects.filter(is_active=True).order_by('title')
    tags = BlogTag.objects.filter(is_active=True).order_by('title')

    paginator = Paginator(all_post,2)
    page = request.GET.get('page',1)  # Paginator , all_post !! 
    allpost = paginator.get_page(page)

    context = dict(
        all_post = allpost,
        categories = categories,
        tags =  tags,
    )
    return render(request,"blog/blog_index.html",context)


def category_view(request, category_slug):
    category = get_object_or_404(BlogCategory, slug = category_slug)
    categories = BlogCategory.objects.filter(is_active=True).order_by('title')
    tags = BlogTag.objects.filter(is_active=True).order_by('title')
    all_post = BlogPost.objects.filter(
        category=category,
        is_active=True).order_by('-created_at')
    
    paginator = Paginator(all_post,2)
    page = request.GET.get('page',1)  # Paginator , all_post !! 
    allpost = paginator.get_page(page)


    context = dict(
        category = category,
        all_post = allpost,
        categories = categories,
        tags =  tags,
    )
    return render(request,"blog/blog_index.html",context)


def blog_detail(request, category_slug, post_slug):
    post = get_object_or_404(BlogPost, slug=post_slug)
    all_post = BlogPost.objects.filter(is_active=True).order_by('-created_at')[:5]
    categories = BlogCategory.objects.filter(is_active = True).order_by('title')[:1]
    tags = BlogTag.objects.filter(is_active = True).order_by('title')

    context = dict(
        categories =categories,
        tags = tags,
        post = post,
        all_post = all_post,
    )
    return render(request,"blog/blog_detail.html",context)

def blog_search(request):
    if "q" in request.GET and request.GET["q"] !="":
        q = request.GET["q"] 
        all_post = BlogPost.objects.filter(is_active=True,title__icontains=q).order_by('-created_at')
        categories = BlogCategory.objects.all()
    else:
        return redirect('/blog')
    
    paginator = Paginator(all_post,2)
    page = request.GET.get('page',1)  # Paginator , all_post !! 
    allpost = paginator.get_page(page)

    context = dict(
        all_post = allpost,
        categories = categories,
    )
    return render(request,"blog/blog_index.html",context)
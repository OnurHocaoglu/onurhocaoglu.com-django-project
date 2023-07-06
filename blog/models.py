from django.db import models
from django.urls import reverse

# AutoSlug enable
from autoslug import AutoSlugField
# Tinymce
from tinymce import models as tinymce_models


class BlogCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:category_view", kwargs={"category_slug": self.slug})
    


class BlogTag(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    tag = models.ManyToManyField(BlogTag)  
    category = models.ForeignKey(BlogCategory,on_delete=models.SET_NULL, null=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    post_img = models.ImageField(upload_to='blogpost')
    content = tinymce_models.HTMLField(blank=True,null=True)
    view_count = models.PositiveBigIntegerField(default=0) # post content view
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            "blog:blog_detail",
            kwargs={
            "category_slug": self.category.slug,
            "post_slug": self.slug,
            })
    
     


from django.contrib import admin
from .models import BlogPost,BlogCategory,BlogTag



@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display =[
        'id',
        'title',
        'is_active',
    ]
    list_display_links =[
        'title',
    ] 


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    pass





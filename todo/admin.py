from django.contrib import admin
from .models import Todo,Category,Tag



class TodoAdmin(admin.ModelAdmin):
    list_display =[
        "pk",
        "title",
        "category",
        "is_active",
        "created_at",
        "updated_at",
    ] 
    list_display_links =[    # Admin panelinde içeriklere Click özelliği getirmek istediğimiz alanlar. 
        "pk",
        "title",           
        "category",
    ] 

class CategoryAdmin(admin.ModelAdmin):
    list_display =[
        "pk",
        "title",
        "slug",
    ]
    list_display_links =[    # Admin panelinde içeriklere Click özelliği getirmek istediğimiz alanlar. 
        "pk",
        "title",           
        "slug",
    ] 

admin.site.register(Todo,TodoAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag)
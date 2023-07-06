from django.contrib import admin
from .models import PageLatesProjects,ContactMe
# Register your models here.

admin.site.register(PageLatesProjects)


@admin.register(ContactMe)
class ContactMeAdmin(admin.ModelAdmin):
    list_display =[
        'id',
        'name',
        'email',
        'subject',
        'message',
    ]
    list_display_links =[
        'name',
        'subject',
        'message',
    ] 
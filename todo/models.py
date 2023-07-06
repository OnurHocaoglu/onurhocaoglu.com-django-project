from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from = 'title', unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("todo:category_detail_view", kwargs={"category_slug": self.slug})
    
class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title", unique=True)# tag slug bilgileri title'dan alacak
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("todo:tag_view", kwargs={"tag_slug": self.slug})

class Todo(models.Model):
   # category = models.ForeignKey(Category, on_delete=models.CASCADE)#  (yabancı anahtar oluşturduk Category ile) kullanılmaz, casecade yapınca category silinirse tüm todolar gider  
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) # ForeignKey oluşturuldu category tablosu ile.
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)# import ettiğimiz django user'ı foreignkey yapıyoruz ve "Cascade" yaparak silindiğinde herşey gitsin diyoruz. 
    tag = models.ManyToManyField(Tag)# tag tablosu ile yabancı anahtar oluşturulur ve bire çok ilişki verilir. (Birden fazla tag olabilir!)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            "todo:todo_detail", 
            kwargs={
            "category_slug": self.category.slug,
            "id": self.id
            }
        )
    
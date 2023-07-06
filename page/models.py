from django.db import models

# Create your models here.

class PageLatesProjects(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='page') # media/page klasörüne import edecek fotografları
    content = models.TextField()
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title
    

class ContactMe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
    


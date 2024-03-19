from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title

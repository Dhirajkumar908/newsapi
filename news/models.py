from django.db import models

# Create your models here.

class contect(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    url=models.URLField()
    comment=models.TextField(max_length=500)
    def __str__(self):
        return self.email
    
class post(models.Model):
   
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    Discription=models.CharField(max_length=350)
    Detailed_post=models.CharField(max_length=1500)
    img=models.ImageField(upload_to='media')
    def __str__(self):
        return self.title
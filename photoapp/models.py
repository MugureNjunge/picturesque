from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse

# Create your models here.

class Location(models.Model):
  title = models.CharField(null=True, blank=True, max_length=200)

  def __str__(self):
    return self.title  

class Category(models.Model):
  title = models.CharField(null=True, blank=True, max_length=200)
 

  def __str__(self):
    return self.title
    

class Image(models.Model):
  squareImage = ResizedImageField(size=(1000,1000), crop=['middle', 'center'], default='default_square_jpg',upload_to='square')
  imageName = models.TextField(null=True, blank=True) 
  description = models.TextField(null=True, blank=True)
  category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
  location = models.ForeignKey(Location,on_delete=models.CASCADE, null=True)
 


  def __str__(self):
        return self.imageName

  def save_image(self):
        self.save()  

  class Meta:
        ordering = ['imageName']    


  @classmethod
  def category(cls):
        category = cls.objects.filter()
        return category

  @classmethod
  def location(cls):
        location = cls.objects.filter()
        return location
     
  
  @classmethod
  def search_by_title(cls,search_term):
      category = cls.objects.filter(title__icontains=search_term)
      return category 

  def search_by_title(cls,search_term):
      location = cls.objects.filter(title__icontains=search_term)
      return location    

  def search_by_title(cls,search_term):
      image_id = cls.objects.filter(title__icontains=search_term)
      return image_id     


    
         
  

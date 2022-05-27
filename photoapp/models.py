from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse

# Create your models here.

class Category(models.Model):
  title = models.CharField(null=True, blank=True, max_length=200)
 

  def __str__(self):
    return self.title
    
         
  # @classmethod
  # def search_by_title(cls,search_term):
  #   title = cls.objects.filter(title=search_term)
  #   return title
      

  # def save(self, *args, **kwargs):
  

class Image(models.Model):
  image = ResizedImageField(size=(1000,1000), crop=['middle', 'center'], default='default_square_jpg',upload_to='square')
  imageName = models.TextField(null=True, blank=True) 
  description = models.TextField(null=True, blank=True)
  category = models.ManyToManyField(Category)
 
#  location = models.ManyToManyField(Location)


  def __str__(self):
        return self.imageName

  def save_image(self):
        self.save()  

  class Meta:
        ordering = ['imageName']    


class Location(models.Model):
  title = models.CharField(null=True, blank=True, max_length=200)

  def __str__(self):
    return self.title        
             


  # @classmethod
  # def mombasa(cls):
  #     mombasa = cls.objects.filter()
  #     return mombasa

  # @classmethod
  # def nairobi(cls):
  #     nairobi = cls.objects.filter()
  #     return nairobi       
         
  

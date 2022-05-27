from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse

# Create your models here.

class Category(models.Model):
  title = models.CharField(null=True, blank=True, max_length=200)
  uniqueId = models.CharField(null=True, blank=True, max_length=100)
  slug = models.CharField(unique=True, blank=True, max_length=500)
 

  def __str__(self):
    return '{} {}'.format(self.title , self.uniqueId)

  def get_absolute_url(self):
    return reverse['category-detail', kwargs={'slug': self.slug}]

  def save(self, *args, **kwargs):
  
    if self.uniqueId is None:
      self.uniqueId = str(uuid4()), split('-')(4)
      self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

      self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
      
      super(Category, self).save(*args, **kwargs)

class Image(models.Model):
  image = ResizedImageField(size=(1000,1000), crop=['middle', 'center'], default='default_square_jpg',upload_to='square')
  imageName = models.TextField(null=True, blank=True) 
  description = models.TextField(null=True, blank=True)
  category = models.ForeignKey(Category, null=True, blank=True, blank=True, on_delete=models.CASACADE)
  location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.CASACADE)
  
class Location(models.Model):
  pass

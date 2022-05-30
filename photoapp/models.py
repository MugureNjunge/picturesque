from django.db import models
from django_resized import ResizedImageField


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

  squareImage = ResizedImageField(size=[2878, 1618], crop=['middle', 'center'], upload_to='square/', blank=True)
  imageName = models.TextField(null=True, blank=True) 
  description = models.TextField(null=True, blank=True)
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  location = models.ForeignKey(Location,on_delete=models.CASCADE)


  def __str__(self):
      return self.imageName


  @classmethod
  def getImages(cls):
      allImages = cls.objects.all()
      return allImages

#  find image
  @classmethod
  def get_findImage(cls,id):
      findImage = cls.objects.filter(image_id=id)
      return findImage

  @classmethod
  def get_location(cls,id):
      location = cls.objects.filter(location_id=id)
      return location

  @classmethod
  def get_category(cls,id):
      category = cls.objects.filter(category_id=id)
      return category


  @classmethod
  def searchImage(cls,search_term):
      searchedImage = cls.objects.filter(category__name__icontains=search_term)
      return searchedImage

from django.db import models
from django_resized import ResizedImageField


# Create your models here.

class Location(models.Model):
  title = models.CharField(null=True, blank=True, max_length=200)

  def __str__(self):
    return self.title  

  def save_category(self):
    self.save()

  def delete_category(self):
    self.delete()
  
  def update_category(self, update):
    self.image_category = update
    self.save()  

class Category(models.Model):
  title = models.CharField(null=True, blank=True, max_length=200)
 

  def __str__(self):
    return self.title

  def save_category(self):
    self.save()

  def delete_category(self):
    self.delete()
  
  def update_category(self, update):
    self.photo_category = update
    self.save()  
  

class Image(models.Model):

  # squareImage = models.ImageField(upload_to='square/', blank=True)
  squareImage = ResizedImageField(size=(1000,1000), crop=['middle', 'center'], default='default_square_jpg',upload_to='square')
  imageName = models.TextField(null=True, blank=True) 
  description = models.TextField(null=True, blank=True)
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  location = models.ForeignKey(Location,on_delete=models.CASCADE)

  def save_image(self):
    self.save()

  def __str__(self):
      return self.imageName

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
  def delete_image(cls, image_id):
      image_to_delete = cls.objects.filter( id=image_id)
      image_to_delete.delete()

  @classmethod
  def searchImage(cls,search_term):
      searchedImage = cls.objects.filter(category__name__icontains=search_term)
      return searchedImage

  @classmethod
  def search_by_category(cls,search_term):
      image = cls.objects.filter(category__name__icontains=search_term)
      return image 

  @classmethod
  def search_by_location(cls,search_term):
      image = cls.objects.filter(location__name__icontains=search_term)
      return image       

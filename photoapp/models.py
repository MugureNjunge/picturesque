from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse

# Create your models here.

class Categories(models.Model):
  title = models.CharField(null=True, blank=True, max_length=200)
  uniqueId = models.CharField(null=True, blank=True, max_length=100)
  slug = models.CharField(unique=True, blank=True, max_length=500)
  date_created = models.DateTimeField(null=True, blank=True)
  last_updated = models.DateTimeField(null=True, blank=True)

  def __str__(self):
    return '{} {}'.format(self.title , self.uniqueId)


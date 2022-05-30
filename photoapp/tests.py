from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class TestCategory(TestCase):
    def setUp(self):
        self.category_trial = Category(category_name="category food")

    def test_category_instance(self):
        self.assertTrue(isinstance(self.category_trial, Category))

class TestLocation(TestCase):
    def setUp(self):
        self.location_trial = Location(location="local")

    def test_location_instance(self):
        self.assertTrue(isinstance(self.location_trial, Location))

class TestImage(TestCase):
    def setUp(self):
        self.category_trial = Category(category_name="category food")
        self.category_trial.save()
        
        self.location_trial = Location(location="international")
        self.location_trial.save()
        
        self.image_trial = Image(pin_name="pin",pin_description="abcdef",category=self.category_trial,location=self.location_trial,pin_image='../media/square/food1.jpeg')
        
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_image_instance(self):
        self.assertTrue(isinstance(self.image_trial, Image))
        
    def test_save_images(self):
        self.image_trial.save_image()
        all_images = Image.objects.all()
        self.assertTrue(len(all_images) == 1)
        
    def test_delete_image(self):
        self.image_trial.save_pin()
        self.image_trial.delete_image(self.image_trial.id)
        self.assertTrue(len(Image.objects.all()) == 0)
   
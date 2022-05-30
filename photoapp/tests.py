from django.test import TestCase
from .models import category, Location,Pin

# Create your tests here.
class Testcategory(TestCase):
    def setUp(self):
        self.category_trial = category(category_name="category trial")

    def test_category_instance(self):
        self.assertTrue(isinstance(self.category_trial, category))

class TestLocation(TestCase):
    def setUp(self):
        self.location_trial = Location(location="Cote d'ivoire")

    def test_location_instance(self):
        self.assertTrue(isinstance(self.location_trial, Location))

class TestImages(TestCase):
    def setUp(self):
        self.category_trial = category(category_name="category trial")
        self.category_trial.save()
        
        self.location_trial = Location(location="Cote d'ivoire")
        self.location_trial.save()
        
        self.image_trial = Pin(pin_name="pin",pin_description="abcdef",category=self.category_trial,location=self.location_trial,pin_image='../media/images/bellaciao.jpg')
        
    def tearDown(self):
        category.objects.all().delete()
        Location.objects.all().delete()
        Pin.objects.all().delete()

    def test_image_instance(self):
        self.assertTrue(isinstance(self.image_trial, Pin))
        
    def test_save_pins(self):
        self.image_trial.save_pin()
        all_images = Pin.objects.all()
        self.assertTrue(len(all_images) == 1)
        
    def test_delete_image(self):
        self.image_trial.save_pin()
        self.image_trial.delete_image(self.image_trial.id)
        self.assertTrue(len(Pin.objects.all()) == 0)
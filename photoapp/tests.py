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


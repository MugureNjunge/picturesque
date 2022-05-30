from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class TestCategory(TestCase):
    def setUp(self):
        self.category_trial = Category(category_name="fashion")

    def test_category_instance(self):
        self.assertTrue(isinstance(self.category_trial, Category))


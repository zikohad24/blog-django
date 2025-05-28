from django.test import TestCase
from django.test import TestCase
from .models import Tag

class TagModelTest(TestCase):
    def setUp(self):
        Tag.objects.create(name="Django")

    def test_tag_creation(self):
        tag = Tag.objects.get(name="Django")
        self.assertEqual(tag.name, "Django")

    def test_tag_str_representation(self):
        tag = Tag.objects.get(name="Django")
        self.assertEqual(str(tag), "Django")

    def test_tag_name_unique(self):
        with self.assertRaises(Exception):
            Tag.objects.create(name="Django")

# Create your tests here.

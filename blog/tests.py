from django.test import TestCase
from .models import Author, Tag, Post
from datetime import date
from django.utils.text import slugify

class AuthorModelTest(TestCase):
    def test_author_str(self):
        author = Author.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="jane@example.com"
        )
        self.assertEqual(str(author), "Jane Doe")

class TagModelTest(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="python")
        self.assertEqual(str(tag), "python")

class PostModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="Test",
            last_name="User",
            email="test@example.com"
        )
        self.tag1 = Tag.objects.create(name="django")
        self.tag2 = Tag.objects.create(name="testing")

        self.post = Post.objects.create(
            title="Post de prova",
            excerpt="Resum del post de prova",
            content="Contingut complet del post",
            image_name="example.jpg",
            date=date.today(),
            author=self.author
        )
        self.post.tags.add(self.tag1, self.tag2)

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Post de prova")
        self.assertEqual(self.post.author.first_name, "Test")
        self.assertIn(self.tag1, self.post.tags.all())
        self.assertIn(self.tag2, self.post.tags.all())

    def test_post_slug_generated(self):
        self.assertEqual(self.post.slug, slugify("Post de prova"))

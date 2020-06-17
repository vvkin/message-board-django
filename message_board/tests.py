from django.test import TestCase
from django.urls import reverse
from .models import Post

class TestHomePage(TestCase):
    def setUp(self):
        Post.objects.create(text='text', title='title')

    def test_home_page_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_new_name_response(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class TestPostModel(TestCase):
    def setUp(self):
        Post.objects.create(text='text', title='title')

    def test_model_creating(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.text, 'text')
        self.assertEqual(post.title, 'title')

from django.test import TestCase
from . models import Post
class ModelTesting(TestCase):

    def setUp(self):
        self.blog = Post.objects.create(number="8")

    def test_post_model(self):
            d= self.blog
            self.assertTrue(isinstance(d,Post))
            self.assertEqual(str(d),"8")

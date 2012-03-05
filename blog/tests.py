from django.test import TestCase

from blog.models import Post


class SimpleTest(TestCase):
    def test_permalink(self):
        p = Post(title='test', slug='slug', body='body')
        p.save()
        url = p.get_absolute_url()

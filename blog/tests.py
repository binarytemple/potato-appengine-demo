import datetime

from django.test import TestCase
from django.utils.unittest.case import expectedFailure
from django.core.urlresolvers import reverse

from blog.models import Post


post_attrs = dict(
    title='title',
    slug='slug',
    date=datetime.datetime.now(),
    teaser = 'teaser',
    body = 'body',
)


class PostUniquenessTests(TestCase):
    """ Exploratory testing to discover how using GAE's Datastore affects a
    simple blogging app.
    
    """
    
    
    @expectedFailure
    def test_slugfield_uniqueness_on_save(self):
        """ In a Django app using an RDBMS, we would expect the save operation
        to fail because of the duplicate slug - using GAE this is not the case.
        
        """
        p1 = Post(**post_attrs)
        p1.save()
        
        p2 = Post(**post_attrs)
        self.assertRaises(Exception, p2.save)
    
    
    @expectedFailure
    def test_slugfield_uniqueness_on_retrieval(self):
        """ The implementation of the Python library for GAE is such that the
        use of a QuerySet's get() method will still raise an Exception when
        muliple objects are returned as a result of the above.
        
        """
        p1 = Post(**post_attrs)
        p1.save()
        
        p2 = Post(**post_attrs)
        p2.save()
        
        recovered = Post.objects.get(slug='slug')



class ViewTests(TestCase):
    """ Simple tests to verify that, minimally, our views respond with good
    status codes - quickly catches TemplateSyntaxErrors and the like.
    
    """
    
    
    def test_list_view(self):
        res = self.client.get(reverse('post_list'))
        self.assertEqual(res.status_code, 200)
    
    
    def test_detail_view(self):
        p = Post(**post_attrs)
        p.save()
        res = self.client.get(p.get_absolute_url())
        self.assertEqual(res.status_code, 200)
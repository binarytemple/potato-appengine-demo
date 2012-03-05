from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    teaser = models.TextField(
        help_text='A short introduction to the Post, as RestructuredText.')
    body = models.TextField(
        help_text='The main body of the Post, as RestructuredText.')
    author = models.ForeignKey(User, null=True, blank=True, editable=False)
    
    
    @models.permalink
    def get_absolute_url(self):
        return ('post_detail', (), {
                'year': '%(year)04d' % {'year': self.date.year },
                'slug': self.slug,
                })
    
    
    def __unicode__(self):
        return self.title
    
    
    class Meta(object):
        ordering = ('-date',)
from django.conf.urls.defaults import *

from blog.views import PostListView, PostDetailView

urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<slug>.+)/$', PostDetailView.as_view(), name='post_detail'),
)
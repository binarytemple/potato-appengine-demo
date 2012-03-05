from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView

from blog.models import Post

class PostListView(ListView):
    queryset = Post.objects.order_by('-date')
    context_object_name = 'posts'
    template_name = 'post_list.html'
    paginate_by = 10


class PostDetailView(DetailView):
    context_object_name = 'post'
    template_name = 'post_detail.html'
    
    def get_object(self):
        return Post.objects.get(date__year=self.kwargs.get('year'),
                                slug=self.kwargs.get('slug'))
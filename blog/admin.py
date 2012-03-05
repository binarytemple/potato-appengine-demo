from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    model = Post
    
    fieldsets = ((None, {
        'fields': ('title', 'slug')
    }),
    ('Content', {
         'classes': ('monospace',),
         'fields': ('teaser', 'body')
     }),)
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)
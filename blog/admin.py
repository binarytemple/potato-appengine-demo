from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    model = Post
    
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = ((None, {
        'fields': ('title', 'slug')
    }),
    ('Content', {
         'classes': ('monospace',),
         'fields': ('teaser', 'body')
     }),)
    
    
    def save_model(self, request, obj, form, change):
        """ Automatically save the author of the Post when it is saved in the
        admin.
        
        """
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Post, PostAdmin)
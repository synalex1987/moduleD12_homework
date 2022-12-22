from django.contrib import admin
from .models import Post, PostCategory, PostCounter

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'preview_for_admin_panel')
    list_filter = ('author', )
    search_fields = ('title', 'text',)


#admin.site.register(Post)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(PostCounter)
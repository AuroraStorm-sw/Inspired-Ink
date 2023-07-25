from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


"""
The PostAdmin class contains ways to filter through
and search for specific blog posts with different
fields, also tells the admin panel what section
that Summernote should be applied to, in this case the
content text field.
"""

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


"""
Likewise to the PostAdmin class, the Comment class
contains ways to filter through and search for
specific blog posts with different fields.
It also contains the "actions", in which the admin can
approve individual comments.
"""


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

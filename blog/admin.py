from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


"""
The PostAdmin class tells the admin panel what section
that Summernote should be applied to, in this case the
content text field.
"""

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')


admin.site.register(Comment)

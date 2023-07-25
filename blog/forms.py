from .models import Comment, Post
from django import forms


class AddInk_form(forms.ModelForm):
    """
    Form model that allows authenticated users to
    write and post posts
    """
    class Meta:
        model = Post
        fields = ('author', 'title', 'content',)


class FeedbackForm(forms.ModelForm):
    """
    Form model that allows authenticated users to
    leave feedback on posts
    """
    class Meta:
        model = Comment
        fields = ('body',)
from .models import Comment, Post
from django import forms


class AddInkForm(forms.ModelForm):
    """
    Form model that allows authenticated users to
    write and post posts
    """
    class Meta:
        model = Post
        fields = ('author', 'category', 'title', 'excerpt', 'content',)

        widgets = {
            'excerpt':  forms.Textarea(
                attrs={'placeholder': 'Write a short description'})

        }


class EditInkForm(forms.ModelForm):
    """
    Form model that allows authenticated users to
    edit their posts
    """
    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'content',)


class FeedbackForm(forms.ModelForm):
    """
    Form model that allows authenticated users to
    leave feedback on posts
    """
    class Meta:
        model = Comment
        fields = ('body',)

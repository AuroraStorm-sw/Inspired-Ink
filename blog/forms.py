from .models import Comment
from django import forms


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
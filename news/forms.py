from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    A form for creating and editing Comment instances,
    exposing only the 'body' field.
    """
    class Meta:
        model = Comment
        fields = ('body',)
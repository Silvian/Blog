from django import forms
from .models import Comment
from django.forms.widgets import HiddenInput


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields["blog"].widget = HiddenInput()

    class Meta:
        model = Comment
        fields = ('author', 'text', 'blog',)

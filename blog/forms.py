from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={'class': 'comment-input'}))

    class Meta:
        model = Comment
        fields = ['content']

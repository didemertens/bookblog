from django import forms
from .models import Blog, Comment

class PostForm(forms.ModelForm):

  class Meta:
    model = Blog
    fields = ('title', 'intro','body')

    widgets = {
    'title': forms.TextInput(attrs={'class': 'post-title'}),
    'intro': forms.Textarea(attrs={'class': 'post-intro'}),
    'body': forms.Textarea(attrs={'class': 'post-content'}),
    }

class CommentForm(forms.ModelForm):

  class Meta:
    model = Comment
    fields = ('text',)

    widgets = {
    'text': forms.Textarea(attrs={'class': 'text-comment'}),
    }



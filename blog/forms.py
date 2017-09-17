from django.contrib.auth.models import User
from django import forms
from .models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['commenter', 'comment_content']


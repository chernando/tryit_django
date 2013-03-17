# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Post


class CommentForm(forms.Form):

    content = forms.CharField(widget=forms.Textarea)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('author',)

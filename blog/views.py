# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import CommentForm, PostForm
from .models import Post, Comment


def index(request):
    last_posts = Post.objects.order_by('-pk')[:5]
    context = {'posts': last_posts}

    return render(request, 'blog/post_list.html', context)


@login_required
def post_create(request):
    base = Post(author=request.user)
    form = PostForm(request.POST or None, instance=base)

    if form.is_valid():
        post = form.save()
        return HttpResponseRedirect(post.get_absolute_url())
    else:
        return render(request, 'blog/post_create.html', {'form': form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm()
    context = {'post': post, 'form': form}

    return render(request, 'blog/post_detail.html', context)


@login_required
def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = Comment()
        comment.author = request.user
        comment.post = post
        comment.content = form.cleaned_data['content']
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    else:
        return render(request, 'blog/post_detail.html',
                      {'post': post, 'form': form})


def alive(request):
    '''For devops' talk'''
    return HttpResponse('Ok')

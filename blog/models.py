# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=45)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()

    @property
    def comments(self):
        return self.comment_set.count()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', args=[self.pk])


class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    content = models.TextField()

# -*- coding: cp1251 -*-

from django.db import models, connection
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from control_panel.settings import MEDIA_ROOT
from django.core.urlresolvers import reverse

# Create your models here.
import datetime


class Author(models.Model):

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(null=True)
    birthyear = models.IntegerField(null=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):

    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey('Publisher')
    publication_date = models.DateField(default=datetime.datetime.now())
    description = models.TextField(null=False, blank=False, default="")

    def get_absolute_url(self):
        curson = connection.cursor()
        curson.execute("SELECT id FROM library_book WHERE title = %s", [self.title])
        return "/library/books/%s/" % curson.fetchall()[0]

    def __unicode__(self):
        return self.title


class Publisher(models.Model):

    title = models.CharField(max_length=32)
    address = models.TextField()
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    website = models.URLField(max_length=32)

    def __unicode__(self):
        return u'%s (%s, %s)' % (self.title, self.city, self.country)


class BookImage(models.Model):

    avatar = models.ImageField(upload_to=MEDIA_ROOT)
    object_id = models.PositiveIntegerField()
    fkey = models.ForeignKey(Book)
    content_type = models.ForeignKey(ContentType)
    content_object = generic.GenericForeignKey("content_type", "object_id")

    def __unicode__(self):
        return '%s' % self.id

    def avatar_count(self):
        count = 0
        if self.avatar:
            count += 1
        return '%s' % count

    def show_avatar(self):
        return u'<img src="%s"/>' % (self.avatar.url)
    show_avatar.allow_tags = True

from django.db import models
from django.contrib import admin
from library.models import Book

# Create your models here.
import datetime


class Customer(models.Model):

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    address = models.TextField()
    is_approved = models.BooleanField()
    email = models.EmailField(null=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Order(models.Model):

    itemld = models.ForeignKey(Book)
    created = models.DateField(default=datetime.datetime.now())
    customer = models.ForeignKey(Customer)

    def __unicode__(self):
        return self.itemld

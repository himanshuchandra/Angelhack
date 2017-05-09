# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

id = int('0')

choice = (
    ('Neutral', 'Neutral'),
    ('Positive', 'Positive'),
    ('Negative', 'Negative')
)


def upload_location(instance, filename):
    global id
    new_id = id + 1
    id = id + 1
    return "%s/%s" % (new_id, filename)


def upload_location_image(instance, filename):
    print "entering"
    global id
    new_id = id + 1
    id = id + 1
    print new_id , filename
    return "uploaded/%s/%s" % (new_id, filename)


# by age , gender , location
class Company(models.Model):
    cname = models.CharField(max_length=100)
    cslug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.cname


class Product(models.Model):
    pkey = models.ForeignKey(Company, on_delete=models.CASCADE)
    pname = models.CharField(max_length=100)
    pslug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __unicode__(self):
        return self.pname


class TextRating(models.Model):
    city = models.CharField(max_length=100)
    pkey = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

    def __unicode__(self):
        return self.pkey.pname + " " + self.rating


class EmotionRating(models.Model):
    city = models.CharField(max_length=100)
    pkey = models.ForeignKey(Product, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=100)
    emotion_image = models.ImageField(upload_to=upload_location_image,
                                      null=True,
                                      blank=True,
                                      width_field="width_field",
                                      height_field="height_field"
                                      )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

    def __unicode__(self):
        return self.pkey.pname + " " + self.emotion


def create_pslug(instance, new_slug=None):
    slug = slugify(instance.pname)
    return slug


def create_cslug(instance, new_slug=None):
    slug = slugify(instance.cname)
    return slug


def ppre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.pslug:
        instance.pslug = create_pslug(instance)


def cpre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.cslug:
        instance.cslug = create_cslug(instance)


pre_save.connect(cpre_save_post_receiver, sender=Company)
pre_save.connect(ppre_save_post_receiver, sender=Product)

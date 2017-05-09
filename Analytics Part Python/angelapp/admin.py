# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Company, Product, TextRating, EmotionRating


admin.site.register(Company)
admin.site.register(Product)
admin.site.register(TextRating)
admin.site.register(EmotionRating)


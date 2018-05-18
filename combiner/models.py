# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
"""
from mongoengine import *

class IngredientMongo(Document):
    name = fields.StringField(required=True)
    description = fields.StringField(required=True)

class DrinkMongo(Document):
    name = fields.StringField(required=True)
    description = fields.StringField(required=True, null=True)
    ingredient_list = fields.ListField(fields.ReferenceField(Ingredient))
"""

class Drink(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1024)
    image = models.URLField(max_length=512, default='')

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    size = models.IntegerField()
    drink = models.ForeignKey(Drink, related_name='ingredient_list')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import mongoengine

class Ingredient(mongoengine.Document):
    name = mongoengine.fields.StringField(required=True)
    description = mongoengine.fields.StringField(required=True)

class Drink(mongoengine.Document):
    name = mongoengine.fields.StringField(required=True)
    description = mongoengine.fields.StringField(required=True, null=True)
    ingredient_list = mongoengine.fields.ListField(mongoengine.fields.ReferenceField(Ingredient))

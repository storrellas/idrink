# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from rest_framework import viewsets
from rest_framework.response import Response

from combiner.models import Drink
from combiner.serializers import DrinkSerializer

class IndexView(TemplateView):
    template_name = "index.html"

class DrinkViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Drink.objects.all()        
        queryset = sorted(queryset, key=lambda x: random.random())
        serializer = DrinkSerializer(queryset, many=True)
        return Response(serializer.data)

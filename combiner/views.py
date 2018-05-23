# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Python includes
import random, time, json
from threading import Timer

# Django
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView

# DRF includes
from rest_framework import viewsets
from rest_framework.response import Response

#import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


# Project includes
from combiner.models import Drink, Serving
from combiner.serializers import DrinkSerializer
from combiner.serializers import ServingCreateSerializer,ServingSerializer

class IndexView(TemplateView):
    template_name = "index.html"

class DrinkViewSet(viewsets.ViewSet):
    """
    Retrieve current drinks in DB
    """
    def list(self, request):
        count = self.request.query_params.get('count')
        queryset = Drink.objects.all()[:count]  # Limiting number of elements if any
        queryset = sorted(queryset, key=lambda x: random.random())
        serializer = DrinkSerializer(queryset, many=True)
        return Response(serializer.data)


class ServingViewSet(viewsets.ViewSet):
    """
    Viewset to get and create Servings
    """
    def drink_serving_completer(self):
        print "Updating all servings to True ... ", time.time()
        Serving.objects.filter().update(completed=True)
        #Timer(5, drink_serving_completer).start()

    def create(self, request):

        # Create Drink
        serializer = ServingCreateSerializer(data=request.data)
        serializer.is_valid()
        serving = Serving(drink_id=serializer.validated_data['drink'])
        serving.save()

        # Fake MQTT
        #Timer(5, self.drink_serving_completer).start()

        # MQTT publish message
        message = { 'id': serving.id, 'sender': 'pumpclient/1/1'}
        publish.single("pumpcontroller/1/1", json.dumps(message))

        # Generate response
        serializer = ServingSerializer(serving)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        serving = Serving.objects.get(id=pk)
        serializer = ServingSerializer(serving)
        return Response(serializer.data)

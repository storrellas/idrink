from django.conf.urls import url

from rest_framework import routers

from . import views

# Router for DRF
router = routers.SimpleRouter()
router.register(r'drink', views.DrinkViewSet, base_name='drink')
router.register(r'serving', views.ServingViewSet, base_name='serving')


# Set URL patterns
urlpatterns = []
urlpatterns += router.urls
urlpatterns += url('', views.IndexView.as_view()),


#######################################
# Fake code that should be removed
#######################################

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

import time
from threading import Timer

from models import Serving

def drink_serving_completer():
    #print "Updating all servings to True ... ", time.time()
    #logger.info("Updating all servings to True")
    Serving.objects.filter().update(completed=True)
    Timer(5, drink_serving_completer).start()
drink_serving_completer()
#######################################

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

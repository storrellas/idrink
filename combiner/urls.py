from django.conf.urls import url

from . import views

urlpatterns = [
    url('drink/', views.DrinkViewSet.as_view({'get': 'list'}), name='drink-list'),
    url('', views.IndexView.as_view()),
]

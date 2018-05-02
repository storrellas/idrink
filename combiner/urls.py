from django.conf.urls import url

from . import views

urlpatterns = [
    url('^sample/', views.SampleView.as_view()),
    url('', views.IndexView.as_view()),
]

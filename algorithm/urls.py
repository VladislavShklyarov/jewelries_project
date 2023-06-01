from django.urls import path
from . import views
urlpatterns = [
    path('algorithm', views.algorithm, name='algorithm'),
    path('results', views.result, name='result'),
    ]
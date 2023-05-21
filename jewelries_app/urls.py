from django.urls import path
from . import views
urlpatterns = [
    path('astro', views.astro, name='astro'),
    path('kamni', views.kamni,  name='kamni'),
    path('', views.main,  name='main'),
    path('progect', views.progect,  name='progect'),
    path('samocv', views.samocv,  name='samocv'),
    path('algorithm', views.algorithm, name='algorithm')
    ]
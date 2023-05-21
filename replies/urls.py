from django.urls import path
from . import views
urlpatterns = [
    path('', views.create_reply, name='create_reply'),
    ]
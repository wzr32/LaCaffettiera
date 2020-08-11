from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('store/', store, name="store"),
    path('about/', history, name="about"),
    path('sample/', sample, name="sample"),
]
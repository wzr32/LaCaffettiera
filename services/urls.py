from django.urls import path
from .views import *

urlpatterns = [
    path('', services, name="services"),
]
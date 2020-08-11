from django.urls import path
from .views import *

urlpatterns = [
    path('<int:page_id>', page, name="page"),
]
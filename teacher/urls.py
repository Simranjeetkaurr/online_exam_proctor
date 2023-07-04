from django.urls import path
from .views import *

urlpatterns = [
    path("teacher", t_index, name="teacher"),
    path('create_category/', create_category, name='create_category'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path("student", st_index, name="student"),
    path("test", test, name="test"),
]
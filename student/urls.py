from django.urls import path
from .views import *

urlpatterns = [
    path("student", st_index, name="student"),
    path("proctoring/<int:exam_id>", proctoring, name="proctoring"),
    path("thankyou", thankyou, name="thankyou"),
]
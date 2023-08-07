from .views import *
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.urls.conf import include
from django.conf.urls.static import static 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("", include("questions.urls")),
    path("", include("student.urls")),
    path("", include("teacher.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

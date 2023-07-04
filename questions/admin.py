from django.contrib import admin
from .models import *
from django.apps import apps

admin.site.site_header = "Online Exam System Admin"
admin.site.site_title = "Online Exam System Admin Portal"
admin.site.index_title = "Welcome to Online Exam System Admin Portal"

for model in apps.get_app_config('questions').models.values():
    admin.site.register(model)
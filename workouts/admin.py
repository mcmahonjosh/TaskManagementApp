from django.contrib import admin
from . import models
from .models import Event

# Register your models here.
admin.site.register(models.Workout)
admin.site.register(Event)
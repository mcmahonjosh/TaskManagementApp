from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Workout(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()

  author = models.ForeignKey(User, on_delete=models.CASCADE)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def get_absolute_url(self):
      return reverse("workouts-detail", kwargs={"pk": self.pk})

  def __str__(self):
    return self.title
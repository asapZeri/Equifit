from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Addhorse(models.Model):
    horseName = models.CharField(max_length=100)
    horseAge = models.PositiveIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.horseName
class Workout(models.Model):
    date = models.DateField()
    workout_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.workout_type} on {self.date}"


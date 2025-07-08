from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Addhorse(models.Model):
    horseName = models.CharField(max_length=100)
    horseAge = models.PositiveIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(upload_to='horse_pics/', blank=True, null=True)

    def __str__(self):
        return self.horseName
class Workout(models.Model):
    class TrackCondition(models.TextChoices):
        DRY = 'dry','Dry/Hard'
        WET = 'wet' , 'Wet/Muddy'
        GOOD = 'good', 'Perfect'
    class workoutType(models.TextChoices):
        TROT = 'trot', 'Trot'
        GALLOP = 'gallop', 'Gallop'
        LOPE = 'lope', 'Fast Gallop'
        LIGHTBREEZE = 'lightbreeze', 'Light Breeze'
        FULLSPRINT = 'fullsprint', 'Full Sprint'
    class wraps(models.TextChoices):
        COTTONWRAPPED = 'cottonwrapper', 'Cotton Wrapped'
        VETTAPE = 'vettape' , 'Vet Wrap Tape'
        NONE = 'none', 'Not Wrapped'
    horse = models.ForeignKey(Addhorse, on_delete=models.CASCADE, related_name='workouts')
    date = models.DateField()
    workout_type = models.CharField(
        max_length=20,
        choices=workoutType.choices
    )
    duration_minutes = models.PositiveIntegerField()
    notes = models.TextField(blank=True)
    track_condition = models.CharField(
        max_length=10,
        choices=TrackCondition.choices,
        default=TrackCondition.DRY
    )
    wrapped = models.CharField(
        max_length=20,
        choices=wraps.choices,
        default=wraps.NONE
    )    
    def __str__(self):
        return f"{self.workout_type} on {self.date} for {self.horse.horseName}"
    
class Addrace(models.Model):
    class raceType(models.TextChoices):
        CHIEF = 'chief', 'Chief Race'
        RELAY = 'relay', 'Relay Race'
    race = models.CharField(
        max_length=20,
        choices=raceType.choices
    )
    date = models.DateField()
    horse = models.ForeignKey(Addhorse, on_delete=models.CASCADE, related_name='races')
    notes = models.TextField(blank=True)
    name_of_race = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.race} at {self.name_of_race} on {self.date} for {self.horse.horseName}"
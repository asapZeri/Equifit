from django import forms
from .models import Addhorse , Workout, Addrace

class HorseForm(forms.ModelForm):
    class Meta:
        model = Addhorse
        fields = ['horseName', 'horseAge', 'profile_pic']


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'workout_type', 'duration_minutes', 'notes', 'track_condition', 'wrapped']

class RaceForm(forms.ModelForm):
    class Meta:
        model = Addrace
        fields = ['race', 'name_of_race', 'date' , 'notes']
from django import forms
from .models import Addhorse , Workout

class HorseForm(forms.ModelForm):
    class Meta:
        model = Addhorse
        fields = ['horseName', 'horseAge']


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'workout_type', 'duration_minutes', 'notes', 'track_condition']

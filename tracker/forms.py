from django import forms
from .models import Addhorse

class HorseForm(forms.ModelForm):
    class Meta:
        model = Addhorse
        fields = ['horseName', 'horseAge']
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Workout , Addhorse
from .forms import HorseForm
from django.shortcuts import get_object_or_404

@login_required
def home(request):
    workouts = Workout.objects.all().order_by('-date')
    horses = Addhorse.objects.filter(owner=request.user)
    return render(request, 'tracker/home.html', {'horses': horses})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'tracker/login.html', {'form': form})
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})
def add_horse(request):
    if request.method == 'POST':
        form = HorseForm(request.POST)
        if form.is_valid():
            horse = form.save(commit=False)
            horse.owner = request.user 
            horse.save()
            return redirect('home')
    else:
        form = HorseForm()
    return render(request, 'tracker/addhorse.html', {'form': form})

    


    



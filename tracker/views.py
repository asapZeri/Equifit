from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Workout , Addhorse
from .forms import HorseForm, WorkoutForm
from django.shortcuts import get_object_or_404
from django.contrib import messages

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
@login_required
def horse_detail(request, horse_id):
    horse = get_object_or_404(Addhorse, id=horse_id, owner=request.user)
    workouts = horse.workouts.all().order_by('-date')
    return render(request, 'tracker/horse_details.html', {'horse': horse, 'workouts': workouts})


@login_required
def edit_horse(request, horse_id):
    horse = get_object_or_404(Addhorse, id=horse_id, owner=request.user)
    if request.method == 'POST':
        form = HorseForm(request.POST, instance=horse)
        if form.is_valid():
            form.save()
            return redirect('horse_detail', horse_id=horse_id)
    else:
        form = HorseForm(instance=horse)

    return render(request, 'tracker/edit_horse.html', {'form': form, 'horse': horse})


@login_required
def add_workout(request, horse_id):
    horse = get_object_or_404(Addhorse, id=horse_id, owner=request.user)
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.horse = horse
            workout.save()
            return redirect('horse_detail', horse_id=horse.id)
    else:
        form = WorkoutForm()

    return render(request, 'tracker/add_workout.html', {'form': form, 'horse': horse})

#Workout details view

@login_required
def workout_detail(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, horse__owner=request.user)
    return render(request, 'tracker/workout_details.html', {'workout': workout})

#Edit workout flow
@login_required
def edit_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, horse__owner=request.user)

    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout_detail', workout_id=workout.id)
    else:
        form = WorkoutForm(instance=workout)

    return render(request, 'tracker/edit_workout.html', {'form': form,'workout': workout})
@login_required
def delete_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, horse__owner=request.user)

    if request.method == 'POST':
        horse_id = workout.horse.id
        workout.delete()
        messages.success(request, "Workout Has Been Deleted.")
        return redirect('horse_detail', horse_id=horse_id)
    return render(request, 'tracker/delete_workout.html', {'workout': workout})

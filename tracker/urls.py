from django.urls import path
from .views import login_view, home , register_view, add_horse, workout_detail
from . import views


urlpatterns = [
    path('', register_view, name='register'),
    path('register/', register_view),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('add-horse/', add_horse, name='add_horse'),
    path('horse/<int:horse_id>/', views.horse_detail, name="horse_detail"),
    path('horse/<int:horse_id>/edit/', views.edit_horse, name="edit_horse"),
    path('horse/<int:horse_id>/add_workout/', views.add_workout, name='add_workout'),
    path('workout/<int:workout_id>/', views.workout_detail, name='workout_detail'),
    path('workout/<int:workout_id>/edit/', views.edit_workout, name='edit_workout'),
    path('workout/<int:workout_id>/delete/', views.delete_workout, name='delete_workout'),
]

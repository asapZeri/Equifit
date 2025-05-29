from django.urls import path
from .views import login_view, home , register_view, add_horse


urlpatterns = [
    path('', register_view, name='register'),  # <-- base route points to register
    path('register/', register_view),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('add-horse/', add_horse, name='add_horse'),
]

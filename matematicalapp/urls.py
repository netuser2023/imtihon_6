from django.urls import path
from .views import main
urlpatterns = [
    path('matematic/', main, name='matematical'),
]
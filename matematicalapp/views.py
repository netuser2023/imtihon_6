from django.shortcuts import render
from .models import Matematic

# Create your views here.

def main(request):
    matem = Matematic.objects.all()
    return render(request, 'index.html', {'matem': matem})
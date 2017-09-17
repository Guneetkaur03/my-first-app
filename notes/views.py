from django.shortcuts import render
from .models import note
from django.utils import timezone
# Create your views here.

def index(request):
    notes = note.objects.all()
    return render(request, 'notes/index.html', {'notes':notes})

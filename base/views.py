from django.shortcuts import render
from .models import Room

# Create your views here.
def home(request):
    rooms = [
        {'id': 1, 'name': 'Harry'},
        {'id': 2, 'name': 'Ron'},
        {'id': 3, 'name': 'Hermione'},
        {'id': 4, 'name': 'Draco'},
        {'id': 5, 'name': 'Luna'},
    ]

    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None

    room = int(pk)

    context = {'room': room}
    return render(request, 'base/room.html', context)
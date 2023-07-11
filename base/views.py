from django.shortcuts import render

# Create your views here.
def home(request):
    rooms = ['Harry', 'Ron', 'Hermoine', 'Draco', 'Albus']

    context = {'rooms': rooms}
    return render(request, 'home.html', context)

def room(request, pk):
    context = {'id': pk}
    return render(request, 'room.html', context)
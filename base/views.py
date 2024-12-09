from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
rooms=[
    {'id':1, 'name':'let\s learn python'},
    {'id':2, 'name':'Design with me'},
    {'id':3, 'name':'Frontend developers'},
]

def home(request):
    context={'rooms':rooms}
    return render(request, 'base/home.html',context)

def room(request, pk):
    room = None
    for r in rooms:
        if r['id'] == int(pk):
            room = r
            break

    if room:
        context = {'room': room}
        return render(request, 'base/room.html', context)
    else:
        # Handle the case where the room is not found
        return render(request, '404.html', status=404)
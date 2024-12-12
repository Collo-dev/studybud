from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Room,Topic
from .forms import RoomForm

# Create your views here.
# rooms=[
#     {'id':1, 'name':'let\s learn python'},
#     {'id':2, 'name':'Design with me'},
#     {'id':3, 'name':'Frontend developers'},
# ]

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request, 'Username OR Password does not exist')




        
    context = {}
    return render(request, 'base/login_register.html', context)



def room(request, pk):
    room=Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form=RoomForm()
    if request.method == 'POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    context={'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)

    if request.method=='POST':
        form=RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')


    context={'form':form}
    return render(request,'base/room_form.html', context)

def deleteRoom(request, pk):
    room=Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})







def home(request):
    # Your view logic here, e.g., fetching data from models

    context = {'topics': Topic, 'room_count': room_count, 'rooms': rooms}
    #context = {'message': 'Welcome to StudyBud!'}  # Example context data
    return render(request, 'base/home.html', context)
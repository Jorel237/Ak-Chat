from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Features, posts, Room, Message
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.


def index(request):
    return render(request, 'index.html')

def home(request):
    
    u = User.objects.all()
    f = Features.objects.all()
    p = posts.objects.all() 
    
  
    context = {        
        'fs':f,
        'ps':p,
        'us':u,
        
    }
    
                    
    
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        userName = request.POST['name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        Cpwd = request.POST['Cpwd']
        if pwd == Cpwd:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('signin')
            elif User.objects.filter(username=userName).exists():
                messages.info(request, 'User already exists')
                return redirect('signin')
            else:
                user = User.objects.create_user(username=userName, email=email, password=pwd)
                user.save();
                
                
                
                return redirect('login')
        else:
            messages.info(request, "Password don't macht")
            return redirect('signin')
    else:           
        return render(request, 'signin.html')
def login(request):
    if request.method == 'POST':
        userName = request.POST['name']
        pwd = request.POST['pwd']

        user = auth.authenticate(username=userName, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'No such credetial in our plateform')
            return redirect('login')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return render(request,'error.html')

def entity(request):
    links = [1,2,3,'akuman', 'home']
    context = {
        'links':links
    }
    return render(request, 'entity.html', context)

def profile(request, ak):
    context = {
        'val': ak
    }
    return render(request, 'profile.html', context)

def postz(request, pk):
    postzs = posts.objects.get(id=pk)
    f = Features.objects.all()
    p = posts.objects.all() 
    context = {
        'pz':postzs,        
        'fs':f,
        'ps':p
    }
    return render(request, 'blogs.html', context)

def room(request, room):
    room_detail = Room.objects.get(room=room)
    user = request.GET.get('username')   
    context = {
        'room':room,
        'user':user,
        'room_detaile':room_detail
    }
    
    return render(request, 'room.html', context)

def check(request):   
    room = request.POST['room_name']
    user =  request.POST['username']
    if Room.objects.filter(room=room).exists():
        return redirect('/'+room+'/?username='+user)
    else:
        new_room = Room.objects.create(room=room)
        new_room.save();
        return redirect('/'+room+'/?username='+user)
    
def send(request):
    message =request.POST['message']
    room_id =request.POST['room_id']
    user =request.POST['username']
    
    new_message = Message.objects.create(value=message, user=user, room=room_id)
    new_message.save();
    return HttpResponse('Message have been send')
    
def getMessage(request, room):
    room_detail = Room.objects.get(room=room)
    
    message = Message.objects.filter(room=room_detail.id)
    return JsonResponse({"message":list(message.values())})
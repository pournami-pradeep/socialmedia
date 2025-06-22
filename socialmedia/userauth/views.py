from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import *


# Create your views here.
def home(request):
    user_obj = request.user
    username = user_obj.username
    try:
        profile = Profile.objects.get(user=user_obj).profileimg
    except:
        profile = None
    print(profile)
    posts = Posts.objects.all().order_by()
    return render(request,'main.html',{"username":username,"profile":profile,"posts":posts})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email_id = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            message = "This username is already exist."
            return render(request,'signup.html',{"message":message})
        
        if User.objects.filter(email=email_id).exists():
            message = "Email already registered."
            return render(request,'signup.html',{"message":message})

        user_obj = User.objects.create_user(username,email_id,password)
        profile_obj = Profile.objects.create(user=user_obj,id_user=user_obj.id)
        if user_obj:
            login(request,user_obj)
            return redirect('/')
        return redirect('/')
    
    return render(request,'signup.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = authenticate(request, username=username,password=password)
        if user_obj:
            login(request,user_obj)
            return redirect('/')
        message = "Invalid credentials"
        return render(request,'login.html',{"message":message})
    return render(request,'login.html')


def upload(request):
    if request.method == 'POST':
        username = request.user.username
        post = request.FILES.get("image")
        print(post)
        caption = request.POST.get("caption")
        new_post = Posts.objects.create(user=username,image=post,caption=caption)
        return redirect('/')
    return render(request,'upload.html')


from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.info(request,'User already exist, Please login')
                return redirect('vaccine_app:register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already used try another one')
                return redirect('vaccine_app:register')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                return redirect('vaccine_app:login')
        else:
            messages.info(request,'Password doesnt match')
            return redirect('vaccine_app:register')


    return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Incorrect credentials')
            return redirect('vaccine_app:login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')






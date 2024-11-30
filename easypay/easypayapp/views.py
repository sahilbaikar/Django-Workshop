from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, logout
from django.contrib.auth.decorators import login_required
from .models import Transaction, Userprofile


from django.http import JsonResponse, HttpResponse 


def home(request):
    return render(request, 'easypayapp/index.html')


def about(request):
    return render(request, 'easypayapp/index.html') 

def contact(request):
    return render(request, 'easypayapp/index.html')


def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Check if the username is unique
        if not User.objects.filter(username=username).exists():
            # Create a new user
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=email)

            User_profile = Userprofile.objects.create(username=username,amount_balance=10000)

            return redirect('user_login')  # Redirect to your login view
        else:
            error_message = 'Username already exists'
    else:
        error_message = None

    return render(request, 'easypayapp/register.html',
                  {'error_message': error_message})



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to your dashboard view
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = None

    return render(request, 'easypayapp/login.html',
                  {'error_message': error_message})


def user_logout(request):
    logout(request)
    return redirect('user_login')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate,logout
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after successful registration
            login(request, user)
            return redirect('home') 
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('admin')
            else:

                login(request, user)
                return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'users/signin.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('signin') 

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

def dashboard(request):
    return HttpResponse('user dashboard')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect ('home')

def register(request):
    if request.method != 'POST':
        form = RegisterForm
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=True)
            login(request, new_user)
            messages.success(request, 'Registration successful.')
            return redirect('home')
        else:
            messages.warning(request, 'Registration failed.')

    return render(request, 'registration/register.html', {'form': form})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.contrib.auth import login, logout
from . import forms

def dashboard(request):
    return HttpResponse('user dashboard')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect ('home')

def register(request):
    if request.method != 'POST':
        form = forms.RegisterForm
    if request.method == 'POST':
        form = forms.RegisterForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=True)
            new_user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, new_user)
            messages.success(request, 'Registration successful.')
            return redirect('home')
        else:
            messages.warning(request, 'Registration failed.')

    return render(request, 'registration/register.html', {'form': form})

LoginView.form_class = forms.AuthenticationFormCustomised

PasswordResetView.form_class = forms.PasswordResetFormCustomised

PasswordResetConfirmView.form_class = forms.SetPasswordFormCustomised

PasswordChangeView.form_class = forms.PasswordChangeFormCustomised
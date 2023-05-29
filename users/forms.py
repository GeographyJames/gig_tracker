from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", 'first_name', 'last_name', 'email')
        field_classes = {"username": UsernameField}






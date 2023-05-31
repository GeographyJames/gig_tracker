import django.contrib.auth.forms as auth_forms
from django.contrib.auth.models import User
from django import forms

class RegisterForm(auth_forms.UserCreationForm):

    class Meta:
        model = User
        fields = ("username", 'first_name', 'last_name', 'email')
        field_classes = {"username": auth_forms.UsernameField}
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['username'].widget.attrs['class'] = 'form-control'

        self.fields['first_name'].label = ''
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'first name'
        self.fields['first_name'].required = True

        self.fields['last_name'].label = ''
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'last name'
        self.fields['last_name'].required = True

        self.fields['email'].label = ''
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['email'].required = True

        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'

        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'

class AuthenticationFormCustomised(auth_forms.AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(AuthenticationFormCustomised, self).__init__(*args, **kwargs)
       
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'email or username'

        self.fields['password'].label = ''
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'password'

class PasswordResetFormCustomised(auth_forms.PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetFormCustomised, self).__init__(*args, **kwargs)

        self.fields['email'].label = ''
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'email'

class SetPasswordFormCustomised(auth_forms.SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(SetPasswordFormCustomised, self).__init__(*args, **kwargs)

        self.fields['new_password1'].label = ''
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'new password'

        self.fields['new_password2'].label = ''
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'confirm password'


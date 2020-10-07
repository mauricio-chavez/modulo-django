"""Users app forms"""

from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    """Registers a new user"""
    username = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    password = forms.CharField(
        max_length=255, required=True, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(
        max_length=255, required=True, widget=forms.PasswordInput)

    def clean_username(self):
        """Checks if username is unique"""
        username = self.cleaned_data.get('username')
        user_exists = User.objects.filter(username=username).exists()

        if user_exists:
            raise forms.ValidationError('El nombre de usuario ya existe.')

        return username

    def clean_email(self):
        """Checks if email is unique"""
        email = self.cleaned_data.get('email')
        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            raise forms.ValidationError('El correo ya existe.')

        return email

    def clean(self):
        """Checks if passwords matches"""
        data = self.cleaned_data
        password = data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if not password:
            raise forms.ValidationError('Ingresa una contraseña')
        elif password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return data

    def save(self):
        """Saves user into database"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        return User.objects.create_user(**data)

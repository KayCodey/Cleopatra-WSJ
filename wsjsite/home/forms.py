from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Client 

class SignupForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        labels = {
            "first_name": "Imię",
            "last_name": "Nazwisko",
            "phone_number": "Numer telefonu",
            "email": "Adres e-mail",
            "password": "Hasło"

        }
 
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','password1','password2']
        labels = {
            "username": "Login",
            "email": "Adres e-mail",
            "password1": "Hasło",
            'password2': "Powtórz hasło"

        }


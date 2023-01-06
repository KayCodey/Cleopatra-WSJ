from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



 
class CreateUserForm(UserCreationForm):
    #phone_number = forms.CharField(min_length=9, max_length=11, label='Numer telefonu')
    first_name = forms.CharField(max_length=100, label='Imię')
    last_name = forms.CharField(max_length=100,label='Nazwisko')
    password1 = forms.CharField(label='Hasło',strip=False,
    widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło',strip=False,
    widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=['username','first_name','last_name','email','password1','password2']
        labels = {
            "username": "Login",
            "email": "Adres e-mail"
        }


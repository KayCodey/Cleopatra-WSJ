from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .forms import SignupForm, CreateUserForm
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR,"templates"),'
)

def index(request):
    today = datetime.datetime.now().date()
    return render(request, "home/index.html", {"today": today})

# Sign Up View
def signup(request): 
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST) 
        if form.is_valid(): 
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ user)
        #name = form.cleaned_data.get('first_name') 
        #last_name  = form.cleaned_data.get('last_name')
        #phone = form.cleaned_data.get('phone_number')
        #email_address = form.cleaned_data.get('email')
        #password = form.cleaned_data.get('password') 
        #user = authenticate(name=name, last_name=last_name,phone = phone, email_address = email_address,password=password)
        #user = form.save()
        #login(request, user) 
        #return redirect('home/index.html') 
    context = { 
        'signup_form': form 
    } 
    return render(request, 'home/sign-up.html', context) 
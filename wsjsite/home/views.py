from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm 
 
from .forms import SignUpForm
# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR,"templates"),'
)

def index(request):
    today = datetime.datetime.now().date()
    return render(request, "home/index.html", {"today": today})

# Sign Up View
def signup(request): 
    form = SignUpForm(request.POST) 
    if form.is_valid(): 
        form.save() 
        username = form.cleaned_data.get('username') 
        password = form.cleaned_data.get('password') 
        user = authenticate(username=username, password=password) 
        login(request, user) 
        return redirect('home') 
    context = { 
        'form': form 
    } 
    return render(request, 'home/sign-up.html', context) 
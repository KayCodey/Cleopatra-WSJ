from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import datetime
from .forms import CreateUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
# Create your views here.

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR,"templates"),'
)

def index(request):
    today = datetime.datetime.now().date()
    return render(request, "home/index.html", {"today": today})

# Sign Up 
def signup(request): 
    #if request.user.is_authenticated:
    #    return HttpResponseRedirect("/")
    #else:
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST) 
        if form.is_valid(): 
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ user)
            #return redirect('home/index.html') 
    context = { 
            'signup_form': form 
    } 
    return render(request, 'home/sign-up.html', context) 


#Sign In
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/")
        else:
            messages.info(request, 'Username or password is incorrect')


    context ={}
    return render(request, 'home/sign-in.html', context)


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")

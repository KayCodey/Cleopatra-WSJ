from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
import datetime
from .forms import CreateUserForm
from .models import Service,Products, Employee, Comment
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

#Service View
def services(request):
    service_list = Service.objects.all()
    context = {'service_list': service_list}
    return render(request, 'home/service.html', context)

#Products View
def products(request):
    product_list = Products.objects.all()
    context = {'product_list': product_list}
    return render(request, 'home/products.html', context)

#Employee View
def employees(request):
    employee_list = Employee.objects.all()
    context = {'employee_list': employee_list}
    return render(request, 'home/employee.html', context)

#Comments View
def review(request):
    comment_list = Comment.objects.all()
    context = {'comment_list': comment_list}
    return render(request, 'home/index.html', context)

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

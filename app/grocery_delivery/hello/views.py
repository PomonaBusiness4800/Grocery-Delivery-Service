from django.shortcuts import render, redirect
from .models import Grocerystore, Userpaymentinfo, Address, Deliverydriver, Grocerystoreadd, Groceryitem
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    all_stores = Grocerystore.objects.all
    all_payinfo = Userpaymentinfo.objects.all
    all_addresses = Address.objects.all
    all_drivers = Deliverydriver.objects.all
    all_grocstoreaddresses = Grocerystoreadd.objects.all
    all_groceryitem = Groceryitem.objects.all
    return render(request, 'hello/index.html', {'stores':all_stores, 'paymentInfo':all_payinfo, 'addresses':all_addresses,'drivers':all_drivers,'groceryaddresses':all_grocstoreaddresses, 'groceryitem': all_groceryitem})
@login_required(login_url='loginPage') # only logged in users can see this page
def storeview(request):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.all
    return render(request, 'hello/storeview.html', {'stores':all_stores, 'items':all_items})

@login_required(login_url='loginPage') # only logged in users can see this page
def storelist(request): # if method is get then request.get and get the name of the store to search in database for store to display
    return render(request, 'hello/storelist.html',{})

def register(request):
    if request.user.is_authenticated:
        return redirect('storelist')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username') # createa variable
                messages.success(request, 'Account created for ' + user)
                return redirect('loginPage')
        context = {'form': form}
        return render(request, 'hello/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginPage')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('storelist')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('storelist')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'hello/login.html', context)
# Create your views here.,

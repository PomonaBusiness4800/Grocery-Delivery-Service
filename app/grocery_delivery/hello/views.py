from django.shortcuts import render, redirect
from .models import Grocerystore, Userpaymentinfo, Address, Deliverydriver, Grocerystoreadd, Groceryitem
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, addAddressForm, addPaymentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    all_stores = Grocerystore.objects.all
    all_payinfo = Userpaymentinfo.objects.all
    all_addresses = Address.objects.all
    all_drivers = Deliverydriver.objects.all
    all_grocstoreaddresses = Grocerystoreadd.objects.all
    all_groceryitem = Groceryitem.objects.all
    return render(request, 'hello/index.html', {'stores':all_stores, 'paymentInfo':all_payinfo, 'addresses':all_addresses,'drivers':all_drivers,'groceryaddresses':all_grocstoreaddresses, 'groceryitem': all_groceryitem})

@login_required(login_url='loginPage') # only logged in users can see this page
def vons(request):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.all
    return render(request, 'hello/vons.html', {'stores':all_stores, 'items':all_items})
def vonsCats(request, cats):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.filter(category = cats)
    return render(request, 'hello/vons.html', {'stores':all_stores, 'items':all_items})

@login_required(login_url='loginPage') # only logged in users can see this page
def smart_final(request):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.all
    return render(request, 'hello/smart&final.html', {'stores':all_stores, 'items':all_items})

@login_required(login_url='loginPage') # only logged in users can see this page
def wholefoods(request):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.all
    return render(request, 'hello/wholefoods.html', {'stores':all_stores, 'items':all_items})

@login_required(login_url='loginPage') # only logged in users can see this page
def traderjoes(request):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.all
    return render(request, 'hello/traderjoes.html', {'stores':all_stores, 'items':all_items})

@login_required(login_url='loginPage') # only logged in users can see this page
def food4less(request):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.all
    return render(request, 'hello/food4less.html', {'stores':all_stores, 'items':all_items})

@login_required(login_url='loginPage') # only logged in users can see this page
def ralphs(request):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.all
    return render(request, 'hello/ralphs.html', {'stores':all_stores, 'items':all_items})

@login_required(login_url='loginPage') # only logged in users can see this page
def userprofile(request):
    context = {}
    addresses = Address.objects.filter(auth_user = request.user)
    payments = Userpaymentinfo.objects.filter(auth_user = request.user)
    context ['addresses'] = addresses
    context ['payments'] = payments
    if request.method == "POST":
        if request.POST.get('streetaddress'):
            form = addAddressForm(request.POST or None)
            if form.is_valid():
                print ("valid")
                userid = request.user.id
                userobj = User.objects.get(id = userid)
                instance = form.save(commit = False)
                instance.auth_user = userobj
                instance.save()
                return render(request, 'hello/userprofile.html', context)
            else:
                context = {'form':form}
                return render(request, 'hello/userprofile.html', context)
        if request.POST.get('cardnumber'):
            form = addPaymentForm(request.POST or None)
            print("here")

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
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
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'hello/login.html', context)
# Create your views here.,

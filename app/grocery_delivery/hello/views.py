from django.shortcuts import render, redirect
from .models import User, Grocerystore, Userpaymentinfo, Address, Deliverydriver, Grocerystoreadd, Groceryitem
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView

def index(request):
    all_stores = Grocerystore.objects.all
    all_users = User.objects.all
    all_payinfo = Userpaymentinfo.objects.all
    all_addresses = Address.objects.all
    all_drivers = Deliverydriver.objects.all
    all_grocstoreaddresses = Grocerystoreadd.objects.all
    all_groceryitem = Groceryitem.objects.all
    return render(request, 'hello/index.html', {'allUsers':all_users,'stores':all_stores, 'paymentInfo':all_payinfo, 'addresses':all_addresses,'drivers':all_drivers,'groceryaddresses':all_grocstoreaddresses, 'groceryitem': all_groceryitem})

def storeview(request):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.all
    return render(request, 'hello/storeview.html', {'stores':all_stores, 'items':all_items})
@login_required(login_url='loginPage') # only logged in users can see this page

<<<<<<< HEAD
def storelist(request):
    return render(request, 'hello/storelist.html',{})
=======
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

            if form.is_valid():
                print("valid")
                userid = request.user.id
                userobj = User.objects.get(id = userid)
                instance = form.save(commit = False)
                instance.auth_user = userobj
                instance.save()
                return render(request, 'hello/userprofile.html', context)
            else:
                context = {'form':form}
                return render(request, 'hello/userprofile.html', context)
    else: 
        return render(request, 'hello/userprofile.html', context)
>>>>>>> parent of 9050ad6 (added list of addresses and payments for user profile)

def register(request):
    if request.user.is_authenticated:
        return redirect('storelist')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
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

class SearchResultsView(ListView):
    model = Groceryitem
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = City.objects.filter(
                Q(name__icontains=query) | Q(state__icontains=query)
            )
        return object_list
# Create your views here.,

from django.shortcuts import render, redirect
from .models import Grocerystore, Userpaymentinfo, Address, Deliverydriver, Grocerystoreadd, Groceryitem, Purchaseinfo, PurchaseinfoHasGroceryitem
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, addAddressForm, addPaymentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum

@login_required(login_url='loginPage') # only logged in users can see this page
def index(request):
    all_stores = Grocerystore.objects.all
    all_payinfo = Userpaymentinfo.objects.all
    all_addresses = Address.objects.all
    all_drivers = Deliverydriver.objects.all
    all_grocstoreaddresses = Grocerystoreadd.objects.all
    all_groceryitem = Groceryitem.objects.all
    numberItems = PurchaseinfoHasGroceryitem.objects.count()
    return render(request, 'hello/index.html', {'stores':all_stores, 'paymentInfo':all_payinfo, 'addresses':all_addresses,'drivers':all_drivers,'groceryaddresses':all_grocstoreaddresses, 'groceryitem': all_groceryitem, 'numberItems':numberItems })

@login_required(login_url='loginPage') # only logged in users can see this page
def vons(request):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.all
    user_orders = Purchaseinfo.objects.filter(auth_user = request.user)
    numberItems = PurchaseinfoHasGroceryitem.objects.count()
    print(numberItems)
    return render(request, 'hello/vons.html', {'stores':all_stores, 'items':all_items, 'numberItems':numberItems})
def vonsAddCart(request, item_id):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.all
    product = Groceryitem.objects.get(groceryid = item_id)
    print(product.groceryname)
    store = product.grocerystore_storeid # for mysql you have to create many to many with a connecting table
    user_order, status = Purchaseinfo.objects.get_or_create(grocerystore_storeid=store, auth_user = request.user) # to track the items in the order
    order_item, status = PurchaseinfoHasGroceryitem.objects.get_or_create(purchaseinfo_purchaseid = user_order, groceryitem_groceryid = product) # purchaseinfo will have its id and the id of the orderitem #inside this new table, this is where the purchase info will have its list of items through the connecting table
    if status: 
        user_order.save()
        order_item.save()
    return render(request, 'hello/vons.html', {'stores':all_stores, 'items':all_items})
def vonsSearch(request):
    if request.method == "POST":
        searchkey = request.POST['searchkey']
        all_stores = Grocerystore.objects.all
        all_items = Groceryitem.objects.filter(groceryname__icontains = searchkey)
        return render(request, 'hello/vons.html', {'stores':all_stores, 'items':all_items})
    else: 
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
def smart_finalSearch(request):
    if request.method == "POST":
        searchkey = request.POST['searchkey']
        all_stores = Grocerystore.objects.all
        all_items = Groceryitem.objects.filter(groceryname__icontains = searchkey)
        return render(request, 'hello/smart&final.html', {'stores':all_stores, 'items':all_items})
    else: 
        all_stores = Grocerystore.objects.all
        all_items = Groceryitem.objects.all
        return render(request, 'hello/smart&final.html', {'stores':all_stores, 'items':all_items})
def smartCats(request, cats):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.filter(category = cats)
    return render(request, 'hello/smart&final.html', {'stores':all_stores, 'items':all_items})

@login_required(login_url='loginPage') # only logged in users can see this page
def wholefoods(request):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.all
    return render(request, 'hello/wholefoods.html', {'stores':all_stores, 'items':all_items})
def wholefoodsSearch(request):
    if request.method == "POST":
        searchkey = request.POST['searchkey']
        all_stores = Grocerystore.objects.all
        all_items = Groceryitem.objects.filter(groceryname__icontains = searchkey)
        return render(request, 'hello/wholefoods.html', {'stores':all_stores, 'items':all_items})
    else: 
        all_stores = Grocerystore.objects.all
        all_items = Groceryitem.objects.all
        return render(request, 'hello/wholefoods.html', {'stores':all_stores, 'items':all_items})
def wholefoodsCats(request, cats):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.filter(category = cats)
    return render(request, 'hello/wholefoods.html', {'stores':all_stores, 'items':all_items})

@login_required(login_url='loginPage') # only logged in users can see this page
def traderjoes(request):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.all
    return render(request, 'hello/traderjoes.html', {'stores':all_stores, 'items':all_items})
def traderjoesSearch(request):
    if request.method == "POST":
        searchkey = request.POST['searchkey']
        all_stores = Grocerystore.objects.all
        all_items = Groceryitem.objects.filter(groceryname__icontains = searchkey)
        return render(request, 'hello/traderjoes.html', {'stores':all_stores, 'items':all_items})
    else: 
        all_stores = Grocerystore.objects.all
        all_items = Groceryitem.objects.all
        return render(request, 'hello/traderjoes.html', {'stores':all_stores, 'items':all_items})
def traderjoesCats(request, cats):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.filter(category = cats)
    return render(request, 'hello/traderjoes.html', {'stores':all_stores, 'items':all_items})
@login_required(login_url='loginPage') # only logged in users can see this page
def food4less(request):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.all
    return render(request, 'hello/food4less.html', {'stores':all_stores, 'items':all_items})
def food4lessSearch(request):
    if request.method == "POST":
        searchkey = request.POST['searchkey']
        all_stores = Grocerystore.objects.all
        all_items = Groceryitem.objects.filter(groceryname__icontains = searchkey)
        return render(request, 'hello/food4less.html', {'stores':all_stores, 'items':all_items})
    else: 
        all_stores = Grocerystore.objects.all
        all_items = Groceryitem.objects.all
        return render(request, 'hello/food4less.html', {'stores':all_stores, 'items':all_items})
def food4lessCats(request, cats):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.filter(category = cats)
    return render(request, 'hello/food4less.html', {'stores':all_stores, 'items':all_items})

@login_required(login_url='loginPage') # only logged in users can see this page
def ralphs(request):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.all
    return render(request, 'hello/ralphs.html', {'stores':all_stores, 'items':all_items})
def ralphsSearch(request):
    if request.method == "POST":
        searchkey = request.POST['searchkey']
        all_stores = Grocerystore.objects.all
        all_items = Groceryitem.objects.filter(groceryname__icontains = searchkey)
        return render(request, 'hello/ralphs.html', {'stores':all_stores, 'items':all_items})
    else: 
        all_stores = Grocerystore.objects.all
        all_items = Groceryitem.objects.all
        return render(request, 'hello/ralphs.html', {'stores':all_stores, 'items':all_items})
def ralphsCats(request, cats):
    all_stores = Grocerystore.objects.all
    all_items = Groceryitem.objects.filter(category = cats)
    return render(request, 'hello/ralphs.html', {'stores':all_stores, 'items':all_items})

@login_required(login_url='loginPage') # only logged in users can see this page
def cart(request):
    context = {}
    all_items = Groceryitem.objects.all()
    user_orders = Purchaseinfo.objects.filter(auth_user = request.user)
    all_orderitems = PurchaseinfoHasGroceryitem.objects.all()
    numberItems = PurchaseinfoHasGroceryitem.objects.count()
    totalPrice = 0
    for i in user_orders:
        for j in all_orderitems:
            if i.getPurchaseID() is j.getPurchaseID():
                for m in all_items:
                    if j.getGroceryID() is m.getGroceryID():
                        totalPrice = totalPrice + m.getPrice()
    context['user_orders'] = user_orders
    context['all_items'] = all_items
    context['all_orderitems'] = all_orderitems
    context['numberItems'] = numberItems
    context['totalPrice'] = totalPrice
    return render(request, 'hello/cart.html',context)
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

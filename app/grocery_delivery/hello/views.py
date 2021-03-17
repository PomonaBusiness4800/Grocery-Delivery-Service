from django.shortcuts import render
from .models import User
from .models import Grocerystore
from .models import Userpaymentinfo
from .models import Address
from .models import Deliverydriver
from .models import Grocerystoreadd
from .models import Groceryitem
from .forms import UserForm
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
    return render(request, 'hello/storeview.html',{})
def login(request):
    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'hello/login.html',{}) #can redirect to a new page
    else:
        return render(request, 'hello/login.html',{})
# Create your views here.

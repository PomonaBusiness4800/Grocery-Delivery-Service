from django.shortcuts import render
from .models import User
from .models import Grocerystore
from .models import Userpaymentinfo
from .models import Address
from .models import Deliverydriver
from .models import Grocerystoreadd
from .models import Groceryitem
def index(request):
    all_stores = Grocerystore.objects.all
    all_users = User.objects.all
    all_payinfo = Userpaymentinfo.objects.all
    all_addresses = Address.objects.all
    all_drivers = Deliverydriver.objects.all
    all_grocstoreaddresses = Grocerystoreadd.objects.all
    all_groceryitem = Groceryitem.objects.all
    return render(request, 'hello/index.html', {'allUsers':all_users,'stores':all_stores, 'paymentInfo':all_payinfo, 'addresses':all_addresses,'drivers':all_drivers,'groceryaddresses':all_grocstoreaddresses, 'groceryitem': all_groceryitem})

# Create your views here.

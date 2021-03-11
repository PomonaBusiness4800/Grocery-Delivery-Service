from django.shortcuts import render
from .models import User
from .models import Grocerystore
from .models import Userpaymentinfo
def index(request):
    all_stores = Grocerystore.objects.all
    all_users = User.objects.all
    all_payinfo = Userpaymentinfo.objects.all
    return render(request, 'hello/index.html', {'allUsers':all_users,'stores':all_stores, 'paymentInfo':all_payinfo})

# Create your views here.

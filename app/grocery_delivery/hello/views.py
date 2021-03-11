from django.shortcuts import render
from .models import User
def index(request):
    all_users = User.objects.all
    return render(request, 'hello/index.html', {'allUsers':all_users})

# Create your views here.

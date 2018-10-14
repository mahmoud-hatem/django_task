from django.shortcuts import render
from .models import Account

# Create your views here.

def index(request):
    context = {
        'header': "Django App",
        'title': "Welcome to Accounts App"
    }

    return render(request, "accounts/index.html", context)

def list_accounts(request):
    accounts = Account.objects.all()

    context = {
        'accounts': accounts
    }

    return render(request, "accounts/list.html", context)
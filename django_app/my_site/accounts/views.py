from django.http import HttpResponse

from django.shortcuts import render, redirect
from .models import Account
from .forms import AccountCreationForm
# Create your views here.

def index(request):
    context = {
        'title': "Welcome to Accounts App"
    }

    return render(request, "accounts/index.html", context)

def list_accounts(request):
    accounts = Account.objects.all()

    context = {
        'accounts': accounts
    }

    return render(request, "accounts/list.html", context)

def create_account(request):

    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:list")
    else:
        form = AccountCreationForm()

    context = {
        'form': form,
    }
    return render(request, "accounts/add.html", context)
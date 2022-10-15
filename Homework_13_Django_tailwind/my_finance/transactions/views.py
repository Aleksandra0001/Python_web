from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
@login_required(login_url='auth:login')
def index(request):
    return redirect("transactions:index")


@login_required(login_url='auth:login')
def transactions(request):
    return render(request, "transactions/transactions.html")


@login_required(login_url='auth:login')
def statistics(request):
    return render(request, "transactions/statistics.html")


@login_required(login_url='auth:login')
def create_income_transaction(request):
    return render(request, "transactions/transaction.html")

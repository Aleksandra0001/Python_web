from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Income, Expense


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
    if request.method == 'POST':
        amount = request.POST['amount']
        created_at = request.POST['created']
        description = request.POST['description']
        category = request.POST['category']
        print(amount, created_at, description, category)
        new_income = Income(amount=amount, created_at=created_at, description=description, category=category)
        new_income.user_id = request.user.id
        new_income.save()
        return redirect(reverse('transactions:index'))
    return render(request, "transactions/transaction.html")


@login_required(login_url='auth:login')
def create_expense_transaction(request):
    if request.method == 'POST':
        amount = request.POST.get('amount_exp')
        date = request.POST.get('created_exp')
        desc = request.POST.get('description_exp')
        category = request.POST.get('category_exp')
        print(amount, date, desc, category)
        new_expense = Expense(amount=amount, created_at=date, description=desc, category=category)
        new_expense.user_id = request.user.id
        new_expense.save()
        return redirect(reverse('transactions:index'))
    return render(request, "transactions/transaction.html")

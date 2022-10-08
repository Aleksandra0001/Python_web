from django.shortcuts import render


# Create your views here.
def transactions(request):
    return render(request, "transactions/transactions.html")


def statistics(request):
    return render(request, "transactions/statistics.html")

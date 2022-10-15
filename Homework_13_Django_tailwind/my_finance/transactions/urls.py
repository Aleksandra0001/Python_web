from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path("", views.transactions, name="index"),
    path("statistics/", views.statistics, name="statistics"),
    path('income/', views.create_income_transaction, name='income'),
]

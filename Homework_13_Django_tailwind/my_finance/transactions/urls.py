from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path("", views.transactions, name="index"),
    path("statistics/", views.statistics, name="statistics"),
    path('income/', views.create_income_transaction, name='income'),
    path('expenses/', views.create_expense_transaction, name='expenses'),
    path('delete_income/<int:income_id>/', views.delete_income_transaction, name='delete_income'),
    path('delete_expense/<int:expense_id>/', views.delete_expense_transaction, name='delete_expense'),

]

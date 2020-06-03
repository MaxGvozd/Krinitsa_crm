from django.urls import path
from companies import views

urlpatterns = [
    path('companies/create/', views.create_company),
    path('contracts/create/', views.create_contract),
    path('currency/create/', views.create_currency),
    path('contacts/create/', views.create_contact_person),
    path('banks/create/', views.create_bank),
    path('outlets/create/', views.create_outlet),
    path('accounts/create/', views.create_bank_account),
    path('companies/', views.companies),
    path('contracts/', views.contracts),
    path('currency/', views.currency),
    path('contacts/', views.contacts),
    path('banks/', views.banks),
    path('outlets/', views.outlets),
    path('accounts/', views.accounts)
]
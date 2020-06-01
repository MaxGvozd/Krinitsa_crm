from django.urls import path
from companies import views

urlpatterns = [
    path('create/company/', views.create_company),
    path('create/contract/', views.create_contract),
    path('create/currency/', views.create_currency),
    path('create/contact/', views.create_contact_person),
    path('create/bank/', views.create_bank),
    path('create/outlet/', views.create_outlet),
    path('create/account/', views.create_bank_account)
]
from django.db.models import Q
from django.shortcuts import render, redirect

from companies.forms import CompanyForm, ContractForm, CurrencyForm, Contact_personForm, BankForm, OutletForm, Bank_accountForm
from companies.models import Currency, Contract, Company, Outlet, Bank, Contact_person, Bank_account
from django.views.decorators.http import require_GET


@require_GET
def accounts(request):
    query = request.GET.get("q", "")
    accounts_list = Bank_account.objects.filter(Q(number__icontains=query))
    return render(request, 'accounts_list.html', context={
        "accounts_list": accounts_list
    })


@require_GET
def contacts(request):
    query = request.GET.get("q", "")
    contacts_list = Contact_person.objects.filter(
        Q(first_name__icontains=query) | Q(last_name__icontains=query))
    return render(request, 'contacts_list.html', context={
        "contacts_list": contacts_list
    })


@require_GET
def banks(request):
    query = request.GET.get("q", "")
    banks_list = Bank.objects.filter(Q(name__icontains=query))
    return render(request, 'banks_list.html', context={
        "banks_list": banks_list
    })


def outlets(request):
    query = request.GET.get("q", "")
    outlets_list = Outlet.objects.filter(Q(name__icontains=query))
    return render(request, 'outlets_list.html', context={
        "outlets_list": outlets_list
    })


@require_GET
def currency(request):
    query = request.GET.get("q", "")
    currency_list = Currency.objects.filter(Q(name__icontains=query))
    return render(request, 'currency_list.html', context={
        "currency_list": currency_list
    })


@require_GET
def companies(request):
    query = request.GET.get("q", "")
    companies_list = Company.objects.filter(Q(name__icontains=query))
    return render(request, 'companies_list.html', context={
        "companies_list": companies_list
    })


@require_GET
def contracts(request):
    query = request.GET.get("q", "")
    contracts_list = Contract.objects.filter(Q(name__icontains=query))
    return render(request, 'contracts_list.html', context={
        "contracts_list": contracts_list
    })


def create_company(request):
    if request.method == 'GET':
        form = CompanyForm()
        return render(request, 'companies.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'congratulation.html')
        else:
            return render(request, 'companies.html', context={
                "form": form
            })


def create_contract(request):
    if request.method == 'GET':
        form = ContractForm()
        return render(request, 'contract.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'congratulation.html')
        else:
            return render(request, 'contract.html', context={
                "form": form
            })


def create_currency(request):
    if request.method == 'GET':
        form = CurrencyForm()
        return render(request, 'currency.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'congratulation.html')
        else:
            return render(request, 'currency.html', context={
                "form": form
            })


def create_contact_person(request):
    if request.method == 'GET':
        form = Contact_personForm()
        return render(request, 'contact.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = Contact_personForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'congratulation.html')
        else:
            return render(request, 'contact.html', context={
                "form": form
            })


def create_bank(request):
    if request.method == 'GET':
        form = BankForm()
        return render(request, 'bank.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'congratulation.html')
        else:
            return render(request, 'bank.html', context={
                "form": form
            })


def create_outlet(request):
    if request.method == 'GET':
        form = OutletForm()
        return render(request, 'outlet.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = OutletForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'congratulation.html')
        else:
            return render(request, 'outlet.html', context={
                "form": form
            })


def create_bank_account(request):
    if request.method == 'GET':
        form = Bank_accountForm()
        return render(request, 'account.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = Bank_accountForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'congratulation.html')
        else:
            return render(request, 'account.html', context={
                "form": form
            })

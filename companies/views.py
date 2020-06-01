from django.shortcuts import render, redirect

from companies.forms import CompanyForm, ContractForm, CurrencyForm, Contact_personForm, BankForm, OutletForm, Bank_accountForm


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
            return redirect('/')
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
            return redirect('/')
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
            return redirect('/')
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
            return redirect('/')
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
            return redirect('/')
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
            return redirect('/')
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
            return redirect('/')
        else:
            return render(request, 'account.html', context={
                "form": form
            })

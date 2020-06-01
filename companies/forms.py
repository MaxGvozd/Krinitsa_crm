from django import forms
from companies.models import Bank, Contract, Bank_account, Contact_person, Currency, Company, Outlet


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'


class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'


class Bank_accountForm(forms.ModelForm):
    class Meta:
        model = Bank_account
        fields = '__all__'


class OutletForm(forms.ModelForm):
    class Meta:
        model = Outlet
        fields = '__all__'


class Contact_personForm(forms.ModelForm):
    class Meta:
        model = Contact_person
        fields = '__all__'

from django import forms
from companies.models import Bank, Contract, Bank_account, Contact_person, Currency, Company, Outlet


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        labels = {
            'name': "Наименование",
            'upn': "УНП",
            'contract': "Договор",
            'bank_account': "Номер счёта",
            'address': "Адрес",
            'email': "Email"
        }


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
        labels = {
            'name': "Наименование",
            'number': "Номер",
            'start': "Дата начала действия",
            'end': "Конец действия",
            'due_date_payment': "Количество дней оплаты"
        }


class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'
        labels = {
            'name': "Наименование",
            'address': "Адрес"
        }


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'
        labels = {
            'name': "Наименование",
            'abbreviation': "Сокращенное наименование",
            'capacity': "Разрядность"
        }


class Bank_accountForm(forms.ModelForm):
    class Meta:
        model = Bank_account
        fields = '__all__'
        labels = {
            'number': "Наименование",
            'currency': "Валюта",
            'bank': "Наименование банка",
            'start': "Дата начала",
            'end': "Дата окончания"
        }


class OutletForm(forms.ModelForm):
    class Meta:
        model = Outlet
        fields = '__all__'
        labels = {
            'name': "Наименование",
            'company': "Контрагент",
            'address': "Адрес",
            'contact': "Котактное лицо",
            'telephone': "Номер телефона",
            'email': "Email"
        }


class Contact_personForm(forms.ModelForm):
    class Meta:
        model = Contact_person
        fields = '__all__'
        labels = {
            'first_name': "Имя",
            'last_name': "Фамилия",
            'birthday': "Дата рождения"
        }

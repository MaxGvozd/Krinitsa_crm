from django.contrib import admin
from companies.models import Bank, Bank_account, Currency, Company, Contract, Contact_person, Outlet

admin.site.register(Bank)
admin.site.register(Bank_account)
admin.site.register(Currency)
admin.site.register(Company)
admin.site.register(Contract)
admin.site.register(Contact_person)
admin.site.register(Outlet)

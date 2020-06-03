from django import forms

from events.models import Sale


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'
        exclude = [

        ]
        labels = {
            'company': "Контрагент",
            'outlet': "Торговая точка",
            'warehouse': "Склад",
            'product': "Номенклатура",
            'created_by': "Агент"
        }
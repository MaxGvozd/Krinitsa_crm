from django import forms

from goods.models import Warehouse, Product, Volume


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'
        labels = {
            'name': "Наименование",
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': "Наименование",
            'volume': "Вид объёма",
            'price': "Цена",
            'stock': "Остаток"
        }


class VolumeForm(forms.ModelForm):
    class Meta:
        model = Volume
        fields = '__all__'
        labels = {
            'name': "Наименование",
            'gross_weight': "Масса брутто",
            'net_weight': "Масса нетто",
            'in_packaging': "Количество в месте"
        }

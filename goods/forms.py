from django import forms

from goods.models import Warehouse, Product, Volume


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class VolumeForm(forms.ModelForm):
    class Meta:
        model = Volume
        fields = '__all__'
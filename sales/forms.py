from django import forms
from sales.models import Service_area


class AreaForm(forms.ModelForm):
    class Meta:
        model = Service_area
        fields = '__all__'

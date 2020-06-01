from django import forms
from django.contrib.auth.hashers import make_password

from sales.models import Service_area
from users.models import User


class RegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(),
        label='Подтведите пароль',
        max_length=128
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'telephone',
            'role',
            'service_area',
            'password',
        ]
        exclude = []
        widgets = {
            'password': forms.PasswordInput()
        }
        labels = {
            'first_name': "Имя",
            'last_name': "Фамилия",
            'email': "Email адрес",
            'telephone': "Телефон",
            'role': "Статус",
            'service_area': "Зона обслуживания",
            'password': "Пароль"
        }
        help_texts = {
            'username': ""
        }

    def save(self, commit=True):
        self.cleaned_data['password'] = make_password(
            self.cleaned_data['password']
        )
        return super().save(self)

    def clean(self):
        password = self.data['password']
        password_confirm = self.data['password_confirm']
        if password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают")
        return self.data

    def clean_telephone(self):
        telephone = self.data['telephone']
        if not telephone.isdigit():
            raise forms.ValidationError("Поле должно содердать только цифры!")
        return telephone

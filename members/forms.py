from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label=_('Подразделение'), max_length=255, min_length=4, required=True, help_text='Введите: Подразделение',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите: Подразделение'}))
    password1 = forms.CharField(label=_('Пароль'),
                                widget=(forms.PasswordInput(
                                    attrs={'class': 'form-control'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Подтверждение пароля'), widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text=_('Просто введите тот же пароль, для подтверждения.'))
    username = forms.CharField(
        label=_('Логин'),
        max_length=150,
        help_text=_(
            'Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.'),
        validators=[username_validator],
        error_messages={'unique': _(
            "Пользователь с таким именем уже существует.")},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2',)

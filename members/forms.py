from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label=_(
        'Подразделение'), required=True, help_text='Введите: Подразделение', max_length=250,)
    password1 = forms.CharField(label=_(
        'Password'), help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Повторите пароль'), help_text=_(
        'Просто введите тот же пароль, для подтверждения.'))
    username = forms.CharField(label=_('Логин'), max_length=150, help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
                               validators=[username_validator], error_messages={'unique': _("A user with that username already exists.")},)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Подразделение'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

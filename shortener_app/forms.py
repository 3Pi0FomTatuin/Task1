from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from shortener_app.models import CustomUser


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)
        field_classes = {'username': UsernameField, 'email': forms.EmailField}

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

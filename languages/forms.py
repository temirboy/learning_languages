from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Languages
from django.conf.global_settings import LANGUAGES


class AddLanguageForm(forms.ModelForm):
    name = forms.ChoiceField(
        choices=LANGUAGES,
        widget=forms.Select(attrs=None, choices=LANGUAGES),
    )

    class Meta:
        model = Languages
        fields = ['name']

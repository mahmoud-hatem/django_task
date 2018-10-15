from django import forms
from . import models

class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = models.Account
        fields = ['name', 'email']
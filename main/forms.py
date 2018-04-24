from django import forms
from django.forms import ModelForm
from . models import CoinRedirectModel, BasicUrlModel

class CreateCoinForm(forms.ModelForm):
    class Meta:
        model = CoinRedirectModel
        fields = ('customUrl', 'url1', 'url2')
        labels = {
            'url1': 'Url 1 (Must include http:// or https://)',
            'url2': 'Url 2 (Must include http:// or https://)'
        }

class CreateUrlForm(forms.ModelForm):
    class Meta:
        model = BasicUrlModel
        fields = ('customUrl', 'url')
        labels = {
            'url': 'Url (Must include http:// or https://)',
        }
from django import forms
from .models import Stocks

class StockForm(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = ['ticker']
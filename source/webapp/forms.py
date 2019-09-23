from django import forms
from django.forms import widgets
from webapp.models import CATEGORY_CHOICES


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Product name')
    description = forms.CharField(max_length=2000, required=False, label='Description', widget=widgets.Textarea)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True, label='Category', initial=CATEGORY_CHOICES[0][0])
    count = forms.IntegerField(min_value=0, required=True, label='Count')
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=True, label='Price')




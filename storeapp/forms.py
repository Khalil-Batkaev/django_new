from django import forms
from storeapp import models


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'description', 'price', 'qty']

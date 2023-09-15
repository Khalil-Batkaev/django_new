from django import forms
from storeapp import models


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'description', 'price', 'qty', 'image']


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'description', 'price', 'qty', 'image']

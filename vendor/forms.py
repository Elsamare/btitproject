# vendor/forms.py
from django import forms
from .models import Vendor, Product

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'hotel_name', 'email', 'phone', 'address']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

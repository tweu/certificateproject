from django import forms
from django.forms import fields
from course.models import Product, Brand


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'photo', 'brand')

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name', )
from store.models import Category,Produuct
from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"

        

class ProductaddForm(forms.ModelForm):
    class Meta:
        model=Produuct
        exclude="__all__"
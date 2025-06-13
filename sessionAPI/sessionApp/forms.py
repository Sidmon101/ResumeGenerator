from django import forms

class ItemForm(forms.Form):
    name=forms.CharField(max_length=10)
    quantity =forms.IntegerField()

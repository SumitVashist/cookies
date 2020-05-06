from django import forms
class ItemAddForm(forms.Form):
    itemname=forms.CharField()
    quantity=forms.IntegerField()

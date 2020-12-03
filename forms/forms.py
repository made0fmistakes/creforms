from django import forms

class HelpForm(forms.Form):
    First name=forms.CharField( max_length=100)
    Last name=forms.CharField( max_length=100)
    Email=forms.EmailField(default='')

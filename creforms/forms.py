
from django import forms
from .models import Snippet

class ContactForm(forms.Form):
    name=forms.CharField(label='Your name', max_length=100)
    email=forms.EmailField(label='E-Mail')
    catagory=forms.ChoiceField(choices=[('question','Question'),('other','Other')])
    subject=forms.CharField(required=False)
    body=forms.CharField(widget=forms.Textarea)

class SnippetForm(forms.ModelForm):

    class Meta():
        model=Snippet
        fields=('name','email','body')
        

from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SnippetForm
# Create your views here.
def contact(request):

    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            subject=form.cleaned_data['subject']
            body=form.cleaned_data['body']
            params=[]

            print(name,email,subject,body)


    form=ContactForm()
    return render(request,'contact.html',{'form':form})

def snippet_detail(request):

    if request.method=='POST':
        form=SnippetForm(request.POST)
        if form.is_valid():
            print('VALID')
            form.save()


    form=SnippetForm()
    return render(request,'contact.html',{'form':form})

def help(request):
    return render(request,'help.html')

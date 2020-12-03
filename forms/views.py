from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'home.html')

def help(request):

    if request.method=='POST':
        form=HelpForm(request.POST)
        if form.is_valid():
            First name=form.cleaned_data['First name']
            Last name=form.cleaned_data['Last name']
            Email=form.cleaned_data['Email']


            print(First name,Last name, Email)


    form=HelpForm()
    return render(request,'help.html')


def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1 + val2
    return render(request, 'result.html', {'result':res})

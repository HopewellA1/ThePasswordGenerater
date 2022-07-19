import random
from tkinter import ON
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    Info = {
        "Name":"Hope",
        "Surname":"Any"
    }
    return render(request,'AppPrac1/Home.html',Info)

def Password(request):
    Characters = list('abcdefghiklmnopqrstuvwxyz')
    k = 'abcdefghiklmnopqrstuvwxyz'.upper()
    if request.GET.get('upperCase'):
        Characters.extend(k)
    
    if request.GET.get('Numbers'):
        k = '0123456789'
        Characters.extend(k)
    
    if request.GET.get('Special'):
        k = '!@#$%^&*()_+?/{<}>~,.;:|\\'
        Characters.extend(k)
        
    length = int(request.GET.get('length',8))# 8 represents a default value 
    NewPassword = ''
    for x in range(length):
        NewPassword += random.choice(Characters)
    
    
    if request.GET.get('lowerCase') == ON:
        NewPassword.lower()
    return render(request,'AppPrac1/Password.html',{"Paasword":NewPassword})


def About(request):
    return render(request,'AppPrac1/About.html')

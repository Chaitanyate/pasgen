from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    return render(request,'generator/home.html',{'password':'dwewef34234'})

def password(request):
    #print(request.GET)
    test="test"
    char=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('length'))
    thepass=''
    if request.GET.get('upper'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        char.extend(list('!@#$%^&*_|}{'))

    if request.GET.get('number'):
        char.extend(list('0123456789'))



    for x in range(length):
        thepass+=random.choice(char)
    return render(request,'generator/password.html',{'password':thepass,'length1':length})
def about(request):
    return render(request,'generator/about.html')
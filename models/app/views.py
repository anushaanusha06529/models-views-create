from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_author(request):
    name=input('enter a name')
    date=input('enter a date')
    country=input('enter a country')
    email=input('enter a email')
    TOD=Author.objects.get_or_create(name='Anu',date='2024-08-07',country='india',email='anu@gmail.com')
    if TOD[1]:
        return HttpResponse('new name is created')
    else:
        return HttpResponse('new already present')
    


def insert_book(request):
    title=input('enter a title')
    author=input('enter author')
    lto=Author.objects.filter(name=author)
    if lto:
        bko=Book.objects.get_or_create(author=lto[0])
        if bko[1]:
            return HttpResponse('present')
        else:
            return HttpResponse('already exist')
    else:
        return HttpResponse('parent table is not present')    
        
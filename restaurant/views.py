from django.http import HttpResponse
from django.shortcuts import render

def sayHello(request):
    return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})
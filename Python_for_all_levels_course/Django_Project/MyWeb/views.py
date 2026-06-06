from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html',{"key":"I am from Python"})

def downloads(request):
    return HttpResponse('<font face = "sans-serif" color = "navy" size = "7px"><center><h4> No Downloads Available !</h4></center></font>')

def result(request):
    return render(request, 'result.html')





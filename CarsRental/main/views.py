from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def index(request:HttpRequest):
    return render(request,'main/index.html')


def about(request:HttpRequest):
    return render(request,'main/about.html')
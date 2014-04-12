# Create your views here.
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

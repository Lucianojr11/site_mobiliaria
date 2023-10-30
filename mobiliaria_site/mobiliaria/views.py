from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
    return render (request,'index.html')

def properties (request):
    return render (request,'properties.html')

def properties_details (request):
    return render (request,'property-details.html')

def contact(request):
    return render (request,'contact.html')
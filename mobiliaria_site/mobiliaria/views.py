from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import Mensagem
from .models import Message  
from django.contrib import messages
from .forms import ImovelForm

# Create your views here.

def index (request):
    return render (request,'index.html')

def properties (request):
    return render (request,'properties.html')

def properties_details (request):
    return render (request,'property-details.html')

def contact(request):
    return render (request,'contact.html')

def dashboard(request):
    return render (request,'dashboard.html')


def mensagem(request):
    if request.method == 'POST':
        form = Mensagem(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message_content = form.cleaned_data['message']

            # Salvando a mensagem no banco de dados (assumindo que o modelo Message tem os mesmos campos)
            message = Message(name=name, email=email, subject=subject, message=message_content)
            message.save()

            messages.success(request, 'Mensagem enviada!!')
            return redirect('index')

    else:
        form = Mensagem()

    return render(request, 'index.html', {'form': form})


def add_imovel(request):
    # Se o método for POST, precisamos processar os dados do formulário
    if request.method == 'POST':
        form = ImovelForm(request.POST, request.FILES)  

        
        if form.is_valid():
            
            form.save()

           
            return redirect('dashboard')
    else:
       
        form = ImovelForm()

    return render(request, 'dashboard.html', {'form': form})
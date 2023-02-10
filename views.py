from django.shortcuts import render
from django.http import HttpResponse
from .models import Transacao
import datetime
# Create your views here.

def home(request):

    dados = {}
    dados['transacoes'] = Transacao.objects.all()


    return render(request, 'despesa/home.html', dados)

"""Musicgram URL Configuration"""

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect
import json


def index(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hola, Mor querid@, hermos@, delicios@ que mas espero de la vida si no vivir a tu lado, espero que pienses lo mismo  o si no un tiro y pal rio xd! {now}'.format(now=now))

#def inicio(request):
    #return render(request,'inicio.html')

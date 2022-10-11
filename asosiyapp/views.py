from django.shortcuts import render, redirect
from django.views import *

from .models import *
from userapp.models import *


class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'bulimlar.html')
        else:
            return redirect('/')

class MahsulotlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data={
                'mahsulot':Mahsulot.objects.filter(sotuvchi__user=request.user)
            }
            return render(request, 'products.html', data)
        else:
            return redirect('/')

class ClientView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data={
                'client':Mijoz.objects.filter(sotuvchi__user=request.user)
            }
            return render(request, 'clients.html', data)
        else:
            return redirect('/')
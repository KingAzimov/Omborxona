from django.shortcuts import render, redirect
from django.views import *

from .models import *
from statsapp.models import *

class StatistikaView(View):
    def get(self, request):
        if request.user.is_authenticated:
            statistikalar  = Statistika.objects.all()
            qidiruv_sozi=request.GET.get('soz')
            if qidiruv_sozi is not None:
                statistikalar = statistikalar.filter(mahsulot__nom__contains=
                qidiruv_sozi)|statistikalar.filter(mahsulot__brand__contains=
                qidiruv_sozi)|statistikalar.filter(mijoz__nom__contains=
                qidiruv_sozi)
            data={
                'stats': statistikalar
            }
            return render(request, 'stats.html', data)
        else:
            return redirect('/')
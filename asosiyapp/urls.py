from django.urls import path
from django.views import View
from .views import *

urlpatterns = [
    path('', BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('clientlar/', ClientView.as_view(), name='clientlar')
]

from django.shortcuts import render
from .table import shopTable
from .models import Shop

def index(request):
    table = shopTable(Shop.objects.all())
    return render(request, 'base.html', {'table': table})



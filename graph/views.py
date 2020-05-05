from django.shortcuts import render
from django.views.generic import ListView
from .models import Shop
from .script import purge

class ShopList(ListView):
	model = Shop
	template_name = 'table.html'
	ordering = ['id']

def index(request):
	purge()
	return render(request, 'update.html')

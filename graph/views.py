from django.shortcuts import render
from django.views.generic import ListView
from .models import Shop
from .script import purge
from .scraper import scraper
import datetime

class ShopList(ListView):
	model = Shop
	template_name = 'table.html'
	ordering = ['date']

def index(request):
	scraper()
	purge()
	return render(request, 'update.html')

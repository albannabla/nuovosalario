from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Shop
from .script import purge
from .scraper import scraper
import datetime
from django.db.models import Avg, Func


class ShopList(ListView):
	model = Shop
	template_name = 'table.html'
	ordering = ['date']

def index(request):
	scraper()
	purge()
	return render(request, 'update.html')

class Round(Func):
	function = 'ROUND'
	template = '%(function)s(%(expressions)s, 0)'

class avg(TemplateView):
	template_name = "average.html"
	title = "Average Price per Sqm by Date"

	def shops(self):
		return Shop.objects.values('date').annotate(averageprice = Round(Avg('pricepersqm')))


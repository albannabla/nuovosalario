from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Shop
from .script import purge
from .scraper import scraper
import datetime
from django.db.models import Avg, Func
import plotly.graph_objects as go
import plotly.offline as opy

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

class Graph(TemplateView):
	template_name = 'graph.html'

	def get_context_data(self, **kwargs):
		context = super(Graph, self).get_context_data(**kwargs)
		data = Shop.objects.values('date').annotate(averageprice = Round(Avg('pricepersqm')))
		x = []
		y = []
		for i in range(len(data)): 
			x.append(data[i]['date'])
			y.append(data[i]['averageprice'])
		trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104},mode="lines",  name='1st Trace')
		data=go.Data([trace1])
		layout=go.Layout(title="Average Price Per Sqm", xaxis={'title':'date'}, yaxis={'title':'price per sqm (euro)'})
		figure=go.Figure(data=data,layout=layout)
		div = opy.plot(figure, auto_open=False, output_type='div')
		context['graph'] = div
		return context



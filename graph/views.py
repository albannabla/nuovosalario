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

#class Round(Func):
#	function = 'ROUND'
#	template = '%(function)s(%(expressions)s, 0)'

class avg(TemplateView):
	template_name = "average.html"
	title = "Average Price per Sqm by Date"

	def shops(self):
		return Shop.objects.values('date').annotate(averageprice = Avg('pricepersqm')).order_by('date')

class Graph(TemplateView):
	template_name = 'graph.html'

	def get_context_data(self, **kwargs):
		context = super(Graph, self).get_context_data(**kwargs)
		data = Shop.objects.values('date').annotate(averageprice = Avg('pricepersqm')).order_by('date')
		x = []
		y = []
		rownum = []
		for i in range(len(data)): 
			x.append(data[i]['date'])
			y.append(data[i]['averageprice'])
			rownum.append(Shop.objects.filter(date=data[i]['date']).count()) 

		data=go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104},mode="lines",  name='1st Trace')
		layout=go.Layout(title="Average Price Per Sqm", xaxis={'title':'date'}, yaxis={'title':'price per sqm (euro)'})
		figure=go.Figure(data=data,layout=layout)
		div = opy.plot(figure, auto_open=False, output_type='div')
		context['graph'] = div
		
		data2 = go.Bar(x=x, y=rownum)
		layout2=go.Layout(title="Number of Ads per Date", xaxis={'title':'date'}, yaxis={'title':'number of ads', 'range': [0,20]})
		figure2=go.Figure(data=data2,layout=layout2)
		div2 = opy.plot(figure2, auto_open=False, output_type='div')
		context['graph2'] = div2

		return context



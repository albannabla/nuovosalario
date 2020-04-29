from django.shortcuts import render
from django.views.generic import ListView
from .models import Shop

class ShopList(ListView):
	model = Shop
	template_name = 'base.html'



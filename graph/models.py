from django.db import models
from datetime import date

class Shop(models.Model):
	webid = models.CharField(max_length=35)
	link = models.URLField(max_length=128, blank=True)
	price = models.CharField(max_length=38)
	description = models.CharField(max_length=100)
	area = models.CharField(max_length=32)
	pricepersqm = models.FloatField(max_length=30)
	date = models.DateField(default=date.today)


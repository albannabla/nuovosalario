import django_tables2 as tables
from .models import Shop

class shopTable(tables.Table):
	class Meta:
		model = Shop


from .models import Shop
from django.db.models import Q

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def purge():
	for row in Shop.objects.all().reverse():
		if Shop.objects.filter(webid=row.webid).count() > 1 or is_number(row.price) == False or is_number(row.area) == False:
			row.delete()
		elif float(row.area) < 20 or float(row.price) < 50000 or float(row.price) > 300000 or float(row.pricepersqm) < 1000:
			row.delete()
	for row in Shop.objects.all():
		row.pricepersqm = float(row.price)/float(row.area)
		row.save()
	for row in Shop.objects.filter(Q(description__contains="ttivit") | Q(description__contains="essione")):
		row.delete()








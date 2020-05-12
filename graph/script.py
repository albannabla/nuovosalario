from .models import Shop
from django.db.models import Q

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def purge():
	for webid in Shop.objects.values_list('webid', flat=True).distinct():
		Shop.objects.filter(pk__in=Shop.objects.filter(webid=webid).values_list('id', flat=True)[1:]).delete()
	#for row in Shop.objects.all():
	#	if is_number(row.price) == False or is_number(row.area) == False:
	#		row.delete()
	#	elif float(row.area) < 20 or float(row.price) < 50000 or float(row.price) > 300000:
	#		row.delete()
	#for row in Shop.objects.all():
	#	row.pricepersqm = float(row.price)/float(row.area)
	#	row.save()
	#	if float(row.pricepersqm) < 1000:
	#		row.delete()
	for row in Shop.objects.filter(Q(description__contains="ttivit")):
		row.delete()
	#for row in Shop.objects.filter(Q(description__contains="essione")):
	#	row.delete()







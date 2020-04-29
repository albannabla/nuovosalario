from .models import Shop

def purge():
	for row in Shop.objects.all().reverse():
		if Shop.objects.filter(webid=row.webid).count() > 1:
			row.delete()





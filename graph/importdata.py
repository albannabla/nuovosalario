import pandas as pd
from graph.models import Shop
import os


def ImportData(filename, date):
	data = pd.read_csv("/Users/canzonettaclaudio/Documents/CODING/NuovoSalario/ns_root/graph/"+str(filename)+".csv")
	for i in range(len(data['id'])):
		newinstance = Shop.objects.create(webid=str(data['id'][i]),link=str(data['link'][i]),price=str(data['price'][i]),description=str(data['description'][i]),area=str(data['area'][i]),pricepersqm=0,date=date)
	return
	
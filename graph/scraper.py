#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import requests, os
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
from .models import Shop

def scraper():
	# set current working directory
	os.chdir("/Users/canzonettaclaudio/Documents/CODING/NuovoSalario/ns_root/")

	# determine number of pages
	page = requests.get('https://www.immobiliare.it/Roma/vendita_immobili_commerciali/negozio_locale-Roma.html?criterio=rilevanza&pag=1&idMZona[]=10161')
	contents = page.content
	soup = BeautifulSoup(contents, 'html.parser')
	tot_pages = len(soup.find('ul', class_ = 'pagination__number'))-2

	# build url list
	urls = []
	for i in range(tot_pages):
	    urls.append('https://www.immobiliare.it/Roma/vendita_immobili_commerciali/negozio_locale-Roma.html?criterio=rilevanza&pag='+str(i+1)+'&idMZona[]=10161')

	#initialize lists
	shopids = []
	links = []
	prices = []
	titles = []
	areas = []

	# scrape all pages
	for x in urls: 
	    page = requests.get(x)
	    contents = page.content
	    soup = BeautifulSoup(contents, 'html.parser')
	    listings = soup.find_all('li', class_ ='listing-item')    
	    for shop in listings:
	        if shop.ul is not None: 
	            price = shop.ul.li.text
	            prices.append(price)
	            details = shop.find('sup')
	            if details is not None:
	                area = details.parent.span.text
	            else:
	                area = 0
	            areas.append(area)    
	            titdet = shop.find(class_ = 'descrizione__titolo')
	            if titdet is not None:  
	                title = titdet.text
	                titles.append(title)
	            else:
	                titles.append("no description")
	            link = shop.a['href']
	            links.append(link)
	            shopid = shop.a['id']
	            shopids.append(shopid)

	#build dataframe in pandas for visualization
	test_df = pd.DataFrame({'id': shopids,
	                        'link': links,
	                        'price': prices,
	                        'description': titles,
	                        'area': areas
	                        })

	#clean up data
	test_df['price'] = test_df['price'].str.replace(',', '')
	test_df['price'] = test_df['price'].str.replace('.', '')
	test_df['price'] = test_df['price'].str.replace('€', '')
	test_df['price'] = test_df['price'].str.replace(' ', '')
	test_df['price'] = test_df['price'].str.replace('\n', '')
	test_df['area'] = test_df['area'].str.replace('.', '')


	#export in excel 
	#x = datetime.datetime.now()
	#oggi =str(x.year)+str(x.month) +str(x.day)
	#test_df.to_excel(oggi+".xlsx")

	#print out text to confirm successful scraping 
	#print(test_df.info())

	#save to database
	today = date.today()
	for i in range(len(test_df['id'])):
	    #newinstance = Shop.objects.create(webid="test",link="test3",price="test",description="test",area="test",pricepersqm=0,date="2020-05-05")
	    newinstance = Shop.objects.create(webid=str(test_df['id'][i]),link=str(test_df['link'][i]),price=str(test_df['price'][i]),description=str(test_df['description'][i]),area=str(test_df['area'][i]),pricepersqm=0,date=today)
	
	return





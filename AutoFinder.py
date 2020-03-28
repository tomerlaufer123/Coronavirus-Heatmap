from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import re

listOfUrls = []

my_url = 'http://www.co.monterey.ca.us/government/departments-a-h/health'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#print(page_html)
page_soup = soup(page_html, "html.parser")

listOfWords = ["Covid-19", "COVID-19", "Corona","Cases"]


listOfUrlsforSite = []
for link in page_soup.findAll('a'):
	for word in listOfWords:
		if word.lower() in str(link.get("href")).lower():
			if("http" in str(link.get("href")) and "pdf" not in str(link.get("href"))):
				listOfUrlsforSite.append(str(link.get("href")))

			elif("/" == str(link.get("href"))[0]) and "pdf" not in str(link.get("href")):
				listOfUrlsforSite.append(my_url + str(link.get("href"))[1:])

listOfUrls.append(min(listOfUrlsforSite, key=len))
for url in listOfUrls:
	print(url)
#print(page_soup)
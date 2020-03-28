from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import re

my_url = 'https://www.cdph.ca.gov/Pages/LocalHealthServicesAndOffices.aspx#'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#print(page_html)
page_soup = soup(page_html, "html.parser")

#print(page_soup)

#page_soup = soup.soup('<html><body><div ')

fileName = "countyWebsites.csv"
f = open(fileName,"w+")

header = "County Name, County URL\n"

f.write(header)

countyList = []

listOfInfo = page_soup.findAll('div',{'class',"ms-rtestate-field"})
#listOfInfo = page_soup.findAll('ul')

for i in listOfInfo:
	container = i.findAll('li')

listOfurls = []
for i in container:
	countyName = ""
	url = ""
	try:
		if("City" not in i.a["title"]):
			countyName = i.a["title"]
			url = i.a["href"]
	except KeyError:
		if("City" not in i.text):
			countyName = i.text.strip()
			url = i.a["href"]
	except:
		continue
	finally:
		if countyName != "" and url != "":
			f.write(countyName+","+url+"\n")
f.close()
	#listOfurls.append(i[i.find('" href="'):'i.find(" target'])
	#children = i.findChildren('li', recursive = True)

	#for child in children:
		#iwant = child.text
		#print(iwant)


#stuff = []

#for container in containers:
#	citysite = container.li.a["title"]
#	stuff.append(citysite)

#print(stuff)

#for page in page_soup.findAll("a", {"title"}):
	#print(page)
	#if("City" not in page):
		#containers.append(page)

#for container in containers:
	#countyList.append(page_soup.find())
	


#print(page_soup)
#for tag in page_soup.findAll(text=lambda text: text):
	#print(tag)
'''
text = page_soup.find_all(text=True and text.parent.name == 'table')

output = ''
blacklist = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head',
	'input',
	'script',
	'div',
	'table',
	'ie:menuitem',
	'a',
	'label',
	'span',
	'form',
	'body',
	'head',
	'style',
	'p',
	'h1',
	'h4',
]

for t in text:
	if t.parent.name not in blacklist:
		output += '{}'.format(t)
		print(t.parent.name)
print(output)
'''



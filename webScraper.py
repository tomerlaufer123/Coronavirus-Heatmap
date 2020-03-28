'''
#####################################
Tomer Laufer
03/27/2020
#####################################
'''

import requests
from bs4 import BeautifulSoup
#python2 OR python3
try:
    from urllib.parse import urljoin
except ImportError:
     from urlparse import urljoin
import re

#tells us which links have been (depth-first) recursively searched
link_dict = dict()

def df_link_search(url):

    #1. check if link has already been searched or add it to dict
    if url in link_dict:
        return
    else:
        link_dict[url] = {"content":[],"date":None}

    #2. search url for specified content
    print("Searching",url,"Coronavirus content...")
    try:
        html_page = requests.get(url).text
        page_soup = BeautifulSoup(html_page,'html.parser')
    except:
        print("This link is invalid.")
        return
    for tag in page_soup.find_all(string=re.compile("Coronavirus|Virus",flags=re.I)):
        ###################
        #TODO
        #store relevant snipits in link_dict[url]={[content],...}
        pass
        ###################

    ###################
    #TODO

    #3. check thru content snipits to find date on content
    #...
    ###################

    #4. find other potential links on this page
    print("Searching for other potential links on this page...")
    ###################
    #TODO
    #refine this search criteria below
    ###################
    for tag in page_soup.find_all(href=re.compile("Coronavirus|Virus",flags=re.I)):
        search_url = tag['href']
        if "rel" in tag.attrs and tag["rel"] != "canonical":
            continue
        #sometimes search url is a rel path
        search_url=urljoin(url,search_url)
        df_link_search(search_url)


    #5. out of links
    print("No more links to search for on",url,".")





#main routine
vc_url = 'https://www.vcemergency.com/'
df_link_search(vc_url)

#print results
for url in link_dict:
    if len(link_dict[url]["content"]) > 0:
        print("--------------------------------------")
        print(link_dict[url]['date'])
        print(url,":\n")
        print(str(link_dict[url])[:300]+"...")

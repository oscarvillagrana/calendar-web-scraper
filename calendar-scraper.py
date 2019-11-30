#!/usr/bin/python

from bs4 import BeautifulSoup
import re
import pandas as pd
import requests


page = "https://www.yoshis.com/calendar.html"
headers = {'User-Agent':'Mozilla/5.0'}

def get_soup():
    session = requests.Session()
    pageTree = session.get(page, headers=headers)
    return BeautifulSoup(pageTree.content, 'html5lib')

pageSoup = get_soup()

# print(pageSoup.pritify())

    """
    TODO: need to make a parser because page is badly formed

    html = urllib2.urlopen(page).read()
    for para in html.split("</p>"):
        if '<p class="lead">' in para:
            abstract=para.split('<p class="lead">')[1:][0]
            print ' '.join(abstract.split("\n"))

    """


"""
# the sections I am scraping
section.date.dtstart
a.event-url

# gets dict[//]:
pageSoup.a.attrs

# gets list of strings
pageSoup.a['class']

# also gets list of strings
pageSoup.a.get_attribute_list('class')   
"""
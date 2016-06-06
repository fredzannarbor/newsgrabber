import urllib2
from bs4 import BeautifulSoup
import requests
import re
import getTechmemeUrls
import getscoopz

## This will basically extract any novel information or scoops from a story.

tmUrls = getTechmemeUrls.TechmemeUrls()
scoop = getscoopz.GetScoopz()

urls = tmUrls.getTechmemeUrls()

i = 0
while i < len(urls):
	info = scoop.getScoopz(urls[i])
	print 'Headline: ' + info[0]
	print info[2]
	i += 1
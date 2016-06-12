import urllib2
from bs4 import BeautifulSoup
import requests
import re
import getTechmemeUrls
import getscoopz
import cues

tmUrls = getTechmemeUrls.TechmemeUrls()
scoop = getscoopz.GetScoopz()

for i in tmUrls.techmemeURLs:
	result = scoop.getScoopz(i[1])
	print result[0] + ": " + i[0]
	print result[1]



# url = raw_input("Please enter a URL\n>")

# print scoop.getScoopz(url)
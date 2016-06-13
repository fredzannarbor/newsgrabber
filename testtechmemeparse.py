import urllib2
from bs4 import BeautifulSoup
import requests
import re
import getTechmemeUrls
import getscoopz
import cues
import getsoup
import fetchquotes
import fetchnames
import getmetadata

scoop = getscoopz.GetScoopz()
quotes = fetchquotes.GetQuotes()
names = fetchnames.NameFinder()
soup = getsoup.GetSoup()
metadata = getmetadata.GetMetadata()


# tmUrls = getTechmemeUrls.TechmemeUrls()
# for i in tmUrls.techmemeURLs:
# 	result = scoop.getScoopz(i[1])
# 	print result[0] + ": " + i[0]
# 	print result[1]



url = raw_input("Please enter a URL\n>")
data = soup.getSoup(url)
paras = metadata.getParas(data)


returner = quotes.getQuotes(paras)
for i in returner:
	print i

# scoops = scoop.getScoopz(url)
# print scoops[0] + ": " + scoops[1]
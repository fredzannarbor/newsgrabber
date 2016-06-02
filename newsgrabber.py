import urllib2
from bs4 import BeautifulSoup
import requests

url = 'http://techcrunch.com/2015/04/02/sources-shyp-is-raising-50-million-at-a-250-million-valuation/'
urlopen = urllib2.urlopen(url)
read = urlopen.read()
soup = BeautifulSoup(read)

paras = soup.find_all('p')

phrases = ['hearing', 'source', 'people', 'familiar', 'person']

array = str(paras).split("<p>")
newarray = []
for i in array:
	for j in phrases:
		if j in i:
			newarray.append(i)

for i in newarray:
	print(i + "\n")
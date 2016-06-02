import urllib2
from bs4 import BeautifulSoup
import requests

## This will basically extract any novel information or scoops from a story.

url = raw_input("Input a URL:\n>")
urlopen = urllib2.urlopen(url)
read = urlopen.read()
soup = BeautifulSoup(read, "html.parser")

paras = soup.find_all('p')

phrases = ['hearing', 'source', 'said the people', 'familiar', 'person']

array = str(paras).split("<p>")
newarray = []
for i in array:
	for j in phrases:
		if j in i:
			newarray.append(i)

for i in newarray:
	print(i + "\n")
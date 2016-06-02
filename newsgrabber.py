import urllib2
from bs4 import BeautifulSoup
import requests
import re

## This will basically extract any novel information or scoops from a story.

url = raw_input("Input a URL:\n>")
urlopen = urllib2.urlopen(url)
read = urlopen.read()
soup = BeautifulSoup(read, "html.parser")

paras = soup.find_all('p')
headline = soup.find_all(class_="lede-headline__highlighted")

phrases = ['hearing', 'source', 'said the people', 'familiar', 'person']

array = str(paras).split("<p>")

newarray = []
for i in array:
	for j in phrases:
		if j in i:
			newarray.append(i)

newstr = ""

for i in newarray:
	newstr += i + "\n\n"

increplace = newstr.replace("Inc. ", "")

newarray = increplace.split('. ')

newstr = ""

for i in newarray:
	newstr += i + ". "

newstr = newstr.replace("</p>, ", "").replace("\u2019", "'").replace("\\xa0", " ").replace(",\n,", "")

print(newstr)

# stringremove2 = stringremove1.replace("</p>", "")
# stringremove3 = stringremove2.replace("\u2019", "'")
import urllib2
from bs4 import BeautifulSoup
import requests
import re

def getScoopz():

	newstr = ""

	url = raw_input("Enter a URL\n>")

	try:	
		opener = urllib2.urlopen(url)
	except:
		return("Can't open the site :(")

	read = opener.read()
	soup = BeautifulSoup(read, "html.parser")

	paras = soup.find_all('p')

	phrases = ['hearing', 'source', 'familiar', 'person', 'matter', 'said the']

	array = str(paras).split("<p>")

	newarray = []
	for i in array:
		for j in phrases:
			if j in i:
				newarray.append(i)

	newerarray = []

	i = 0
	while i < len(newarray):
		if newarray[i] in newerarray:
			pass
		else:
			newerarray.append(newarray[i])
		i += 1

	newarray = newerarray

	newstr = ""

	for i in newarray:
		newstr += i + "\n\n"

	## Take out "Inc" because it's totally unnecessary and also screws up the period split

	increplace = newstr.replace("Inc. ", "")

	newarray = increplace.split('. ')

	newstr = ""

	for i in newarray:
		newstr += i + ". "

	## Remove codes

	newstr = newstr.replace("</p>, ", "").replace("\u2019", "'").replace("\\xa0", " ").replace("\n.","")

	## Remove links

	newstr = re.sub(r'<[^>]*>', '', newstr)

	if newstr != "":
		return(newstr)
	else:
		return("There's no news!")

print(getScoopz())
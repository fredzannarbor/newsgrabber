import urllib2
from bs4 import BeautifulSoup
import requests
import re

def getScoopz():

	newstr = ""

	url = raw_input("Enter a URL\n>")

	try:	
		urlopen = urllib2.urlopen(url)
	except:
		skip = True
		return("Can't open the site :(")
	
	read = urlopen.read()
	soup = BeautifulSoup(read, "html.parser")

	paras = soup.find_all('p')
	publication = soup.find_all('title')

	publications = ["Recode", "TechCrunch", "Bloomberg"]

	pubsplit = str(publication).split(" ")

	for i in pubsplit:
		if i in publications:
			pubreturn = i

	paras = str(paras).replace("Inc. ", "")

	phrases = ['hearing', 'source', 'person familiar', 'person', 'matter', 'said the', 'has learned']

	array = str(paras).split("<p>")

	newarray = []

	for i in array:
		for j in phrases:
			if j in i:
				newarray.append(i)

	splitarray = []

	for i in newarray:
		s_array = i.split(". ")
		for j in s_array:
			for k in phrases:
				if k in j:
					splitarray.append(j)

	newerarray = []

	i = 0
	while i < len(splitarray):
		if splitarray[i] in newerarray:
			pass
		else:
			newerarray.append(splitarray[i])
		i += 1

	newarray = newerarray

	newstr = ""

	for i in newarray:
		newstr += i + "\n"

	## Remove codes

	newstr = newstr.replace("</p>, ", "").replace("\u2019", "'").replace("\\xa0", " ").replace("\n\n.","")

	## Remove links

	newstr = re.sub(r'<[^>]*>', '', newstr)

	if '"' in newstr:
		return("There are no scoops!")

	if newstr != "":
		return(newstr)
	else:
		return("There are no scoops!")

print(getScoopz())
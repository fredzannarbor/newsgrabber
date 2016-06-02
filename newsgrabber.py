import urllib2
from bs4 import BeautifulSoup
import requests
import re

## This will basically extract any novel information or scoops from a story.

def getTechmemeUrls():

	techmeme = urllib2.urlopen("http://techmeme.com/")
	read = techmeme.read()
	soup = BeautifulSoup(read, "html.parser")

	heds = soup.find_all(class_="L4")
	# heds2 = soup.find_all(class_="L2")
	hedstr = ""
	
	for i in heds:
		hedstr += str(i)

	url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', hedstr)

	return(url)

	# for i in heds:
	# 	hedstr += str(i) + "\n"
	# for i in heds2:
	# 	hedstr += str(i) + "\n"

	# # hedstr = re.sub(r'<[^>]*>', '', hedstr)

	# return(hedstr)

def getScoopz():

	url = raw_input("Input a URL:\n>")

	try:	
		urlopen = urllib2.urlopen(url)
	except:
		return("Can't open the site :(")

	read = urlopen.read()
	soup = BeautifulSoup(read, "html.parser")

	paras = soup.find_all('p')
	headline = soup.find_all(class_="lede-headline__highlighted")

	phrases = ['hearing', 'source', 'familiar', 'person', 'matter']

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

	i = 0

	## Get rid of an annoying last period

	while i < len(newarray) - 1:
		newstr += newarray[i] + ". "
		i += 1

	## Remove codes

	newstr = newstr.replace("</p>, ", "").replace("\u2019", "'").replace("\\xa0", " ").replace(",\n,", "")

	## Remove links

	newstr = re.sub(r'<[^>]*>', '', newstr)

	if newstr != "":
		return(newstr)
	else:
		return("There's no news!")

print(getTechmemeUrls())

# stringremove2 = stringremove1.replace("</p>", "")
# stringremove3 = stringremove2.replace("\u2019", "'")
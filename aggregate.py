import urllib2
from bs4 import BeautifulSoup
import requests
import re
import getscoopz

urlinput = raw_input("Please enter a URL\n>")

url = [["Snapchat", urlinput]]

scoop = getscoopz.GetScoopz()

info = scoop.getScoopz(url)

headline = info[0]
publication = info[1]
text = info[2]

print "\nOld:\n"
print info[2]

split = text.split(', ')

phrases = ['hearing', 'source', 'person familiar', 'person', 'matter', 
					'said the', 'has learned', 'not to be named']
checkedsplit = []

for i in split:
	addstring = True
	for k in phrases:
		if k in i:
			addstring = False
	if addstring == True:
		checkedsplit.append(i)

i = 0
newstr = ""

while i < len(checkedsplit):
	newstr += checkedsplit[i] + ", " + publication + " reports."
	i += 1

print "\nNew:\n"
print newstr + "\n"
import urllib2
from bs4 import BeautifulSoup
import requests
import re
import getscoopz

urlinput = raw_input("Please enter a URL\n>")

url = [["Snapchat", urlinput]]

scoop = getscoopz.GetScoopz()

info = scoop.getScoopz(url)
# print info

headline = info[0]
publication = info[1]
text = info[2]
scoopstrue = info[3]

if scoopstrue == True:
	# print "\nOld:\n"
	# print info[2]

	split = text.split('.')

	phrases = ['hearing', 'source', 'person familiar', 'people familiar', 'person', 'matter', 
						'has learned', 'not to be named', 'said the people']
	
	checkedsplit1 = []

	# This fixes the less formal source application

	for i in split:
		if "," not in i:
			checkedsplit1.append(i)

	checkedsplit = []
	newsplit = []
	newersplit = []
	
	for i in split:
		newsplit.append(i.split("."))

	for k in newsplit:
		for i in k:
			newersplit.append(i)

	for i in newersplit:
		addstring = True
		for k in phrases:
			if k in i:
				addstring = False
			elif i == " " or i == "":
				addstring = False
		if addstring == True:
			print i
			checkedsplit1.append(i)

	i = 0
	newstr = ""

	while i < len(checkedsplit):
		newstr += checkedsplit[i] + ", " + publication + " reports. "
		i += 1

	# print "NEW:\n" + newstr + "\n"
else:
	print headline + "\n"
	print "There are no scoops!"
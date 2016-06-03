import urllib2
from bs4 import BeautifulSoup
import requests
import re
import getscoopz

urlinput = raw_input("Please enter a URL\n>")

url = [["Snapchat", urlinput]]

scoop = getscoopz.GetScoopz()

info = scoop.getScoopz(url)

print info

# print "\nOriginal:\n"

# for i in strings:
# 	print i

# split = []

# for i in strings:
# 	split.append(i.split(','))

# phrases = ['hearing', 'source', 'person familiar', 'person', 'matter', 
# 					'said the', 'has learned', 'not to be named']
# checkedsplit = []

# for i in split:
# 	addstring = True
# 	for j in i:
# 		for k in phrases:
# 			if k in j:
# 				addstring = False
# 		if addstring == True:
# 			checkedsplit.append(j)

# i = 0
# newstr = ""

# while i < len(checkedsplit):
# 	newstr += checkedsplit[i] + ", Bloomberg reports. "
# 	i += 1

# print "\nNew:\n"
# print newstr + "\n"
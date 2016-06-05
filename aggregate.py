import urllib2
from bs4 import BeautifulSoup
import requests
import re
import getscoopz

class Aggregator(object):

	def __init__(self):
		pass

	def aggregate(url):

		scoop = getscoopz.GetScoopz()

		info = scoop.getScoopz(url)
		print info

		headline = info[0]
		publication = info[1]
		text = info[2]
		scoopstrue = info[3]

		if scoopstrue == True:
			print "\nOld:\n"
			print info[2]

			split = text.split(', ')

			phrases = ['hearing', 'source', 'person familiar', 'people familiar', 'person', 'matter', 
								'has learned', 'not to be named', 'said the people']
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
					checkedsplit.append(i)

			i = 0
			newstr = ""

			while i < len(checkedsplit):
				newstr += checkedsplit[i] + ", " + publication + " reports. "
				i += 1

			print "NEW:\n" + newstr + "\n"
		else:
			print headline + "\n"
			print "There are no scoops!"
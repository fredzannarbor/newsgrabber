import urllib2
from bs4 import BeautifulSoup
import requests
import re
import cues
import fetchnames
import getsoup
import getmetadata

class GetQuotes(object):

	def __init__(self):

		self.getsoup = getsoup.GetSoup()
		self.namefinder = fetchnames.NameFinder()
		self.getmetadata = getmetadata.GetMetadata()

	def getQuotes(self,paras):

		if paras:

			lastnames = self.namefinder.getLastNames(paras)
			print lastnames
			quotearray = []
			fullquotearray = []

			for i in paras:
				j = 0
				for name in lastnames:
					if name in i:
						namereturn = name
					else:
						namereturn = "Not found"
				while j < len(i):
					if i[j] == '"':
						quoteget = ''
						k = j+1
						while i[k] != '"':
							quoteget += i[k]
							k += 1
						j = k
						quotearray.append([namereturn, re.sub(r'<[^>]*>', '', quoteget)])
					j += 1

			for i in quotearray:
				if 'http' in i[1]:
					pass
				else:
					fullquotearray.append(i)

			return fullquotearray
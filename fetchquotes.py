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

			ignoreterms = ['title', 'caption', 'meta-credit', '_blank', 'google_elide']
			givearray = []
			for i in paras:
				returnarray = []
				namereturn = "Not found"
				j = 0
				while j < len(i):
					if i[j] == '"':
						quoteget = ''
						k = j+1
						startindex = k
						while i[k] != '"':
							quoteget += i[k]
							k += 1
						j = k
						endindex = k
						for name in lastnames:
							if name not in quoteget and name in i:
								namereturn = name
						quoteget = re.sub(r'<[^>]*>', '', quoteget)
						if quoteget not in ignoreterms:
							returnarray.append([namereturn, quoteget, [startindex, endindex]])
						else:
							pass
					j += 1

				# joins the quotes together
					
				quoteadd = ""
				for i in returnarray:
					quoteadd += " " + i[1]
				givearray.append([i[0], quoteadd])


			for i in givearray:
				if 'https' in i[1] or 'http' in i[1]:
					pass
				elif i[1] == '':
					pass
				else:
					fullquotearray.append(i)

			return fullquotearray

	def getProximity(self, para, names, indices):

		# writing a method that determines the general proximity of names and quotes in a sentence

		

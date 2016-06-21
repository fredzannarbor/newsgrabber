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
			quotearray = []
			fullquotearray = []

			ignoreterms = ['title', 'caption', 'meta-credit', '_blank', 'google_elide']
			givearray = []
			for i in paras:

				truename = False
				returnarray = []
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
						coords = [startindex, endindex]

						for name in lastnames:
							if name in i and name not in quoteget:
								truename = True

						if truename:
							namereturn = self.getProximity(i, lastnames, coords)
						else:
							namereturn = "Not found"

						quoteget = re.sub(r'<[^>]*>', '', quoteget)

						if quoteget not in ignoreterms:
							returnarray.append([namereturn, quoteget])
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
		# this is going to be super janky to start and need extensive refining, there are going to be
		# a lot of edge cases to account for. the general idea is the "said ___" should be close enough

		proxarray = []
		distancearray = []

		for i in names:
				
			if i in para:

				j = 0

				# get coords of names in story

				while j < len(para) - len(i):
					if para[j:j+len(i)] == i:
						idx = j
						proxarray.append([i, idx])
					j += 1

		# get the distance to the quote

		if proxarray != []:

			proxcheckarray = []

			for i in proxarray:

				frontdistance = abs(indices[0] - i[1])
				backdistance = abs(indices[1] - i[1])
				distance = min(frontdistance,backdistance)
				proxcheckarray.append([i[0], distance])

			checkdistance = proxcheckarray[0][1]
			namereturn = proxcheckarray[0][0]

			for i in proxcheckarray:

				if i[1] < checkdistance:
					checkdistance = i[1]
					namereturn = i[0]			

			return namereturn

		else:

			return "Not found"

	def updateNameDB(self,name):

		## Updates the database
		pass
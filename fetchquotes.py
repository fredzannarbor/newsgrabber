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
							if name in i:
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
			
			j = 0

			# get coords of names in story

			while j < len(para) - len(i):
				if i[j:j+len(i)] == i:
					idx = j
					proxarray.append([i, idx])
				j += 1

		# get the distance to the quote

		for i in proxarray:

			frontdistance = indices[0] - i[1]
			backdistance = indices[1] - i[1]
			distance = min(frontdistance,backdistance)
			distancearray.append([i[0], distance])

		# score the distances

		i = 0
		while i < len(distancearray)-1:

			if distancearray[i][1] < distancearray[i+1][1]:
				minindex = i
			else:
				minindex = i+1
			i += 1

		# return the name that's closest	

		return distancearray[minindex][0]

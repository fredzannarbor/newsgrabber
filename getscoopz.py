import urllib2
from bs4 import BeautifulSoup
import requests
import re
import cues
import getsoup
import getpublication

class GetScoopz(object):

	def __init__(self):

		self.getsoup = getsoup.GetSoup()
		self.phrasecues = cues.Cues()
		self.getpublication = getpublication.GetPublication()

	def getScoopz(self,url):	

		articlenames = []

		newerstring = ""

		paras = self.getsoup.getSoup(url)

		if paras:

			
			publication = self.getpublication.getPublication(url)
				
			paras = str(paras).replace("Inc. ", "")

			## Fetch the phrases we're looking for on a per-publication basis

			array = str(paras).split("<p>")

			if publication in self.phrasecues.phrases:
				phrases = self.phrasecues.phrases[publication]
			else:
				phrases = self.phrasecues.phrases['General']

			newarray = []

			for i in array:
				for j in phrases:
					if j in i:
						newarray.append(i)

			splitarray = []

			i = 0
			while i < len(newarray):
				s_array = newarray[i].split(". ")
				for j in s_array:
					for k in phrases:
						if k in j:
							splitarray.append(j + ". ")
				i += 1	

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
				newstr += "--- " + i + "\n"

			## Remove codes

			newstr = newstr.replace("</p>, ", "").replace("\u2019", "'").replace("\\xa0", " ")
			newstr = newstr.replace("\n\n.","").replace('\u201c', "").replace('\u201d', "").replace('\u2014',"")

			## Remove links

			newstr = re.sub(r'<[^>]*>', '', newstr)

			if '"' in newstr:
				newstr = "No scoops/nuggets."

			if newstr != "":
				newerstring += newstr
			else:
				newerstring += "No scoops/nuggets"
				scoopstrue = False

			return([publication, newerstring])
		else:
			return('Broken')


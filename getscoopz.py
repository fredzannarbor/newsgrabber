import urllib2
from bs4 import BeautifulSoup
import requests
import re

class GetScoopz(object):

	def __init__(self):

		pass

	def getScoopz(self, url):

		scoopstrue = True

		newerstring = ""

		skip = False

		for k in url:

			headline = k[0]

			try:	
				urlopen = urllib2.urlopen(k[1])
			except:
				skip = True
				newerstring += "\n" + "Can't open the site :("
			
			read = urlopen.read()
			soup = BeautifulSoup(read, "html.parser")

			paras = soup.find_all('p')

			## try to get the name of the publication from the URL

			publications = ["recode", "techcrunch", "bloomberg", "theinformation"]

			pubsplit = k[1].split("//")
			pubsplit = pubsplit[1].split(".")
			for i in pubsplit:
				if i in publications:
					publication = i
				
			paras = str(paras).replace("Inc. ", "")

			phrases = ['hearing', 'source', 'person familiar', 'people familiar', 'matter', 'said the']

			array = str(paras).split("<p>")

			newarray = []

			for i in array:
				for j in phrases:
					if j in i:
						newarray.append(i)

			splitarray = []

			for i in newarray:
				s_array = i.split(". ")
				for j in s_array:
					for k in phrases:
						if k in j:
							splitarray.append(j + ". ")

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
				newstr += i

			## Remove codes

			newstr = newstr.replace("</p>, ", "").replace("\u2019", "'").replace("\\xa0", " ").replace("\n\n.","")

			## Remove links

			newstr = re.sub(r'<[^>]*>', '', newstr)

			if '"' in newstr:
				newstr = "\n" + "There are no scoops!"

			if newstr != "":
				newerstring += "\n" + newstr
			elif skip == True:
				pass
			else:
				newerstring += "\n" + "There are no scoops!"
				scoopstrue = False

		return([headline, publication, newerstring, scoopstrue])
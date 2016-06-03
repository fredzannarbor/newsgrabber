import urllib2
from bs4 import BeautifulSoup
import requests
import re

class GetScoopz(object):

	def __init__(self):

		pass

	def getScoopz(self, url):

		newerstring = ""

		skip = False


		for k in url:

			newerstring += "\n" + "HEADLINE: " + k[0]

			try:	
				urlopen = urllib2.urlopen(k[1])
			except:
				skip = True
				newerstring += "\n" + "Can't open the site :("
			
			read = urlopen.read()
			soup = BeautifulSoup(read, "html.parser")

			paras = soup.find_all('p')

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
							splitarray.append(j)

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
				newstr += i + "\n"

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

		return(newerstring)
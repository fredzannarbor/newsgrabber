import urllib2
from bs4 import BeautifulSoup
import requests
import re

class GetScoopz(object):

	def __init__(self):

		pass

	def getScoopz(self, url):

		newerstring = ""


		for k in url:

			newerstring += "\n" + "HEADLINE: " + k[0]

			try:	
				urlopen = urllib2.urlopen(k[1])
			except:
				newerstring += "\n" + "Can't open the site :(" + "\n"

			read = urlopen.read()
			soup = BeautifulSoup(read, "html.parser")

			paras = soup.find_all('p')
			headline = soup.find_all(class_="lede-headline__highlighted")

			phrases = ['hearing', 'source', 'familiar', 'person', 'matter']

			array = str(paras).split("<p>")

			newarray = []
			for i in array:
				for j in phrases:
					if j in i:
						newarray.append(i)

			newerarray = []

			i = 0
			while i < len(newarray):
				if newarray[i] in newerarray:
					pass
				else:
					newerarray.append(newarray[i])
				i += 1

			newarray = newerarray

			newstr = ""

			for i in newarray:
				newstr += i + "\n\n"

			## Take out "Inc" because it's totally unnecessary and also screws up the period split

			increplace = newstr.replace("Inc. ", "")

			newarray = increplace.split('. ')

			newstr = ""

			i = 0

			## Get rid of an annoying last period

			while i < len(newarray) - 1:
				newstr += newarray[i] + ". "
				i += 1

			## Remove codes

			newstr = newstr.replace("</p>, ", "").replace("\u2019", "'").replace("\\xa0", " ").replace(",\n,", "")

			## Remove links

			newstr = re.sub(r'<[^>]*>', '', newstr)

			if newstr != "":
				newerstring += "\n" + newstr
			else:
				newerstring += "\n" + "There's no news!"

		return(newerstring)
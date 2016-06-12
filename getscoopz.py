import urllib2
from bs4 import BeautifulSoup
import requests
import re
import cues
import fetchnames

class GetScoopz(object):

	def __init__(self):

		pass

	def getSoup(self,url):

		skip = False

		try:	
			urlopen = urllib2.urlopen(url)
		except:
			skip = True

		if skip == False:
			read = urlopen.read()
			soup = BeautifulSoup(read, "html.parser")

			paras = soup.find_all('p')
			return(paras)

		else:
			return None

	def getScoopz(self,url):

		## initialize packages

		phrasecues = cues.Cues()
		namefinder = fetchnames.NameFinder()
		headline = url[0]
		url = url[1]

		articlenames = []

		scoopstrue = True

		newerstring = ""

		paras = self.getSoup(url)

		if paras:

			## try to get the name of the publication from the URL

			# publications = ["recode", "techcrunch", "bloomberg", "theinformation", "vanityfair", 
			# 						"mic", "venturebeat", "arstechnica", "motherboard", "ap", "fusion",
			# 							"anandtech", "engadget", "latimes", "buzzfeed", "wsj", "theverge", 
			# 							"backchannel", "adage", "medium", "govinsider", "cnet", "reuters",
			# 							"pcworld", "statnews"]

			# pubcap = {'recode': 'Recode', 'techcrunch': 'TechCrunch', 'bloomberg': 'Bloomberg', 
			# 				'theinformation': 'The Information', 'vanityfair': 'Vanity Fair',
			# 				'mic': 'Mic', 'venturebeat': 'VentureBeat', 'arstechnica': 'Ars Technica',
			# 				'motherboard': 'Vice Motherboard', 'ap': 'Associated Press',
			# 				'fusion': 'Fusion', 'anandtech': 'AnandTech', 'engadget': 'Engadget',
			# 				'latimes': 'Los Angeles Times', 'buzzfeed': 'BuzzFeed', 
			# 				'wsj': 'The Wall Street Journal', 'theverge': 'The Verge', 'backchannel': 'Backchannel',
			# 				'adage': 'Ad Age', 'medium': 'Medium', 'cnet': 'CNET', 'reuters': 'Reuters',
			# 				'pcworld': "PCWorld", "statnews": "STAT", "Not found": "Couldn't find publication."}

			pubsplit = url.split("//")
			pubsplit = pubsplit[1].split(".")
			
			for i in pubsplit:
				if i in phrasecues.publications:
					publication = i
			try:
				publication = phrasecues.pubcap[publication]
			except:
				publication = "Not found."
				
			paras = str(paras).replace("Inc. ", "")

			## Fetch the phrases we're looking for on a per-publicationb basis

			if publication in phrasecues.phrases:
				phrases = phrasecues.phrases[publication]
			else:
				phrases = phrasecues.phrases['General']

			array = str(paras).split("<p>")

			lastnames = namefinder.getLastNames(namefinder.getNameArray(array))

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

			return([headline, publication, newerstring, scoopstrue])
		else:
			return('Broken')


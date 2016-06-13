import urllib2
from bs4 import BeautifulSoup
import requests
import re
import cues
import getsoup

class GetMetadata(object):

	def __init__(self):

		self.phrasecues = cues.Cues()
		self.getsoup = getsoup.GetSoup()

	def getPublication(self,url):

		pubsplit = url.split("//")
		pubsplit = pubsplit[1].split(".")
		
		for i in pubsplit:
			if i in self.phrasecues.publications:
				publication = i
		try:
			publication = self.phrasecues.pubcap[publication]
		except:
			publication = "Not found."

		return(publication)

	def getParas(self,soup):

		paras = str(soup).replace("Inc. ", "")
		paras = paras.replace("</p>, ", "").replace("\u2019", "'").replace("\\xa0", " ")
		paras = paras.replace("\n\n.","").replace('\u201c', "").replace('\u201d', "").replace('\u2014',"")
		array = str(paras).split("<p>")
		return(array)
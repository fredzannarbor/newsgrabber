import urllib2
from bs4 import BeautifulSoup
import requests
import re
import cues
import getsoup


class GetPublication(object):

	def __init__(self):
		self.getsoup = getsoup.GetSoup()
		self.phrasecues = cues.Cues()

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
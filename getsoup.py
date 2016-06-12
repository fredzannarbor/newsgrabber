import urllib2
from bs4 import BeautifulSoup
import requests
import re
import cues
import fetchnames


class GetSoup():

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
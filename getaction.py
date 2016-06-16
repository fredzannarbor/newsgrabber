import urllib2
from bs4 import BeautifulSoup
import requests
import re
import cues
import fetchnames
import getsoup
import getmetadata

class GetAction(object):

	def __init__(self):

		self.getsoup = getsoup.GetSoup()
		self.namefinder = fetchnames.NameFinder()
		self.getmetadata = getmetadata.GetMetadata()

	def getAnecdote(self, paras):

		pass

		## return anecdotes

	def getAction(self, sentence):

		pass


		## return action

	def rankAction(self, sentences):

		pass

		## return topAction
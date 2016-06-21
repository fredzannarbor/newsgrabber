import urllib2
from bs4 import BeautifulSoup
import requests
import re
import cues
import fetchnames
import getsoup
import getmetadata
import sqlite3

class GetAction(object):

	def __init__(self):

		self.getsoup = getsoup.GetSoup()
		self.namefinder = fetchnames.NameFinder()
		self.getmetadata = getmetadata.GetMetadata()

	def getAnecdote(self, paras):

		pass

		## This is the lead method that will return an anecdote to the overall aggregator
		## The lead anecdote is defined as the anecdote with the highest overall action
		## This method parses through each sentence, looks for verbs, defines the action
		## of the sentence and then grades them against each other to return the top anecdote

		## return anecdotes

	def getAction(self, sentence):

		## This is the method that will interact with with the database of verbs
		## We'll use this to get the action of the anecdote if we decide it's an anecdote
		## From here, we'll return the action of the sentence back to the lead method
		## This method will also call the Count and Action move methods to iterate the database

		pass


		## return action

	def rankAction(self, sentences):

		## This method ranks the actions of an array of potential anectodes that have all
		## already been assigned an action value. It will return the highest-ranking anecdote
		## (or set of anecdotes if the actions are very close to each other)

		pass

		## return topAction

	def moveCount(self, count):

		## This method will increment or decrement the count of the verb appearance in the database

		pass

		## return None

	def moveAction(self, count):

		## This method will increment or decrement the count of the verb action in the database

		pass

		## return None
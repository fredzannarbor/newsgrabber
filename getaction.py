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
		connection = sqlite3.connect("verbs.db")
		self.cursor = connection.cursor()
		self.cursor.execute("SELECT * FROM commonverbs")
		self.verbarray = []
		self.verbs = []
		result = cursor.fetchall()
		
		for i in result:
			self.verbarray.append(i)

		for i in verbarray:
			self.verbs.append(str(i[0]))


	def getAnecdote(self, paras):

		verbcheck = []
		anectodes = []

		if paras:

			for i in paras:

				giveanectode = False
				returnarray = []

				for j in i:

					if j in self.verbs:

						giveanectode = True
						verb = j

				if giveanectode = True:

					action = self.getaction(i, verb)
					
					if action:

						anecdotes.append(i, action)

					else:

						pass

			
			if anecdotes != []
			
				topaction = self.rankaction(anecdotes)

				return topAction

			else:

				return "No action statements"

		else:

			return "No interesting anecdotes"

		## This is the lead method that will return an anecdote to the overall aggregator
		## The lead anecdote is defined as the anecdote with the highest overall action
		## This method parses through each sentence, looks for verbs, defines the action
		## of the sentence and then grades them against each other to return the top anecdote

		## return anecdotes

	def getAction(self, sentence, verb):

		print sentence

		isanecdote = self.isAnecdote()

		if isanecdote:

			self.cursor.execute("SELECT ACTION FROM commonverbs WHERE VERB=?", (verb,))
			action = cursor.fetchall()

			self.moveCount(verb)
			self.moveAction(verb, 'pos')
			
			return action

		else:

			self.moveCount(verb)
			self.moveAction(verb, 'neg')

			return False


		## This is the method that will interact with with the database of verbs
		## We'll use this to get the action of the anecdote if we decide it's an anecdote
		## From here, we'll return the action of the sentence back to the lead method
		## This method will also call the Count and Action move methods to iterate the database

	def rankAction(self, sentences):

		## This method ranks the actions of an array of potential anectodes that have all
		## already been assigned an action value. It will return the highest-ranking anecdote
		## (or set of anecdotes if the actions are very close to each other)

		maxaction = sentences[0]

		i = 1

		while i < len(sentences):

			if maxaction[1] < sentences[i][1]

				maxaction = sentences[i]

			i += 1

		return maxaction

		## return topAction

	def moveCount(self, verb):

		## This method will increment or decrement the count of the verb appearance in the database

		self.cursor.execute("UPDATE COUNT SET COUNT=COUNT+1 WHERE VERB=?", (verb, ))
		connection.commit()

		return None

	def moveAction(self, verb, direction):

		## This method will increment or decrement the count of the verb action in the database

		self.cursor.execute("SELECT ACTION FROM commonverbs WHERE VERB=?", (verb, ))
		counts = self.cursor.fetchall()

		if direction = 'pos':
			counts += 1
		else:
			counts -= 1

		self.cursor.execute("UPDATE ACTION SET ACTION=? WHERE VERB=?", (counts, verb, ))

		cursor.commit()

		return None

	def isAnecdote(self):

		## This method asks if the anecdote is worthwhile

		check = raw_input("Is this a worthwhile anecdote?\n>")
		if check == 'y':
			return True
		else:
			return False
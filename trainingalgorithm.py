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
		self.connection = sqlite3.connect("verbstest.db")
		self.cursor = self.connection.cursor()
		self.cursor.execute("SELECT * FROM commonverbs")
		self.verbarray = []
		self.verbs = []
		result = self.cursor.fetchall()
		
		for i in result:
			self.verbarray.append(i)

		for i in self.verbarray:
			self.verbs.append(str(i[0]))


	def getAnecdote(self, paras):

		verbcheck = []
		anecdotes = []

		if paras:

			for i in paras:

				giveanectode = False
				returnarray = []

				for j in i:

					if j in self.verbs:

						giveanectode = True
						verb = j

				if giveanectode == True:

					action = self.getaction(i, verb)
					
					if action:

						anecdotes.append(i, action)

					else:

						pass

			
			if anecdotes != []:
			
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

			if maxaction[1] < sentences[i][1]:

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
		countsreturn = self.cursor.fetchall()
		for i in countsreturn:
			counts = i[0]

		if direction == 'pos':
			counts += 1
			print "Counts up"
		else:
			print "Counts down"
			counts -= 1

		self.cursor.execute("UPDATE commonverbs SET ACTION=? WHERE VERB=?", (counts, verb, ))

		self.connection.commit()

		return None

	def isAnecdote(self):

		## This method asks if the anecdote is worthwhile

		check = raw_input("Is this a worthwhile anecdote?\n>")
		if check == 'y':
			return True
		else:
			return False

actiontest = GetAction()
url = raw_input("Input a URL:\n>")
urlopen = urllib2.urlopen(url)
read = urlopen.read()
soup = BeautifulSoup(read, "html.parser")
soupnew = soup.find_all('p')
paras = actiontest.getmetadata.getParas(soupnew)
array = []
parasarray = []
i = 0
while i < len(paras):
	passtest = False
	array = paras[i].split(".")
	secondsplit = []
	for j in array:
		secondsplit.append(j.split(" "))
		for k in secondsplit:
			for l in k:
				if l in actiontest.verbs:
					print j
					print "Verb: " + l
					goodaction = raw_input("Is this an action statement with the right verb?\n>")
					if goodaction == 'y':
						actiontest.moveAction(l, 'pos')
					elif goodaction == 's':
						pass	
					else:
						actiontest.moveAction(l, 'neg')
	i += 1
import sqlite3
from sets import Set
import re

class NameFinder(object):

	def __init__(self):

		self.connection = sqlite3.connect("company.db")
		self.cursor = self.connection.cursor()

	def checkName(self, word):
		if word in self.namearray:
			return True
		else:
			return False

	def getNameArray(self,array):
		
		articlenames = []
		idx = 0
		for i in array:
			fresharray = i.split(" ")
			while idx < len(fresharray):
				if self.checkName(fresharray[idx].lower()) == True:
					articlenames.append([fresharray[idx], fresharray[idx+1]])
				idx += 1
		return(articlenames)


	def getLastNames(self, array):

		lastnamesraw = []
		array = self.getNameArray(array)
		for i in array:
			lastnamesraw.append(i[1])

		## Remove commas
		
		nextarray = []
		for i in lastnamesraw:
			nextarray.append(re.sub(r',', '', i))

		nextarray2 = []
		for i in nextarray:
			if i not in nextarray2:
				nextarray2.append(i)

		## remove extraneous words

		finalarray = []
		for i in nextarray2:
			if i != i.lower():
				finalarray.append(i)

		return finalarray
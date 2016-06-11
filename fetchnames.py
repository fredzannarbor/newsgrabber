import csv

class NameFinder(object):

	def __init__(self):

		f = open('names.csv')
		csv_f = csv.reader(f)
		namearray = []
		for row in csv_f:
			for i in row:
				namearray.append(i.lower())

		self.namearray = namearray

	def checkName(self, word):
		if word in self.namearray:
			return True
		else:
			return False

	def getLastNames(self, array):

		lastnamesraw = []
		for i in array:
			lastnamesraw.append(i[1])

		## Remove dupes

		lastnames = []
		for i in lastnamesraw:
			if i not in lastnames:
				lastnames.append(i)
			else:
				pass
		return lastnames
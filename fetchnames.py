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

	def checkName(word):
		if word in self.namearray:
			return True
		else:
			return False
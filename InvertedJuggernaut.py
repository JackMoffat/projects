import csv
from collections import defaultdict


sheet = open("InvJugProgression.csv")
sheetread = csv.reader(sheet, delimiter = ',')

	
class Wave:

	def __init__(self):

		self.name = None
		self.intensity = []
		self.sets = []
		self.reps = []
		self.rest = []
		self.tester = []





wave = Wave()

iRow = 0
for row in sheetread:
	print('row index is ',iRow)
	print(row)
	iRow += 1
	# print(eval('wt.'+x))

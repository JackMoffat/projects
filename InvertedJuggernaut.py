import csv
from collections import defaultdict

sheetlist = []
namelist = []

sheet = open("InvJugProgression.csv")
sheetread = csv.reader(sheet, delimiter = ',')
for row in sheetread:
	sheetlist.append(row)
	if row[0][0].isdigit():
		namelist.append(row[0])
	
class Wave:

	"""working docstring"""

	def __init__(self):
	

		self.Name = None
		self.Tester = []


class Week:

	def __init__(self):

		self.Name = None
		self.Intensity = []
		self.Sets = []
		self.Reps = []
		self.Rest = []




week = Week()

	# print(eval('wt.'+x))

#This currently creates the accumulation waves. accumulation is specified by sheetlist[index+1],the 0-4
##specifiers are for the sparate parameters in their current order
for index, item in enumerate(sheetlist):
	if index % 4 == 0:
		print(sheetlist[index])
		week.Name = sheetlist[index+1][0]
		week.Intensity = sheetlist[index+1][1]
		week.Sets = sheetlist[index+1][2]
		week.Reps = sheetlist[index+1][3]
		week.Rest = sheetlist[index+1][4]


print(week.Name,week.Intensity,week.Sets,week.Reps,week.Rest)






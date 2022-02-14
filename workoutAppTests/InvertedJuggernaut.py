import csv
from collections import defaultdict

sheetlist = []
wavelist = []

sheet = open("InvJugProgression.csv")
sheetread = csv.reader(sheet, delimiter = ',')
for row in sheetread:
	sheetlist.append(row)
	if row[0][0].isdigit():
		wavelist.append(row[0])
	
class Wave:

	"""working docstring"""

	def __init__(self):
	

		self.Name = None
		self.Tester = []

#Need to learn about class inheritance here
class Week(Wave):

	def __init__(self):

		self.Name = None
		self.Intensity = []
		self.Sets = []
		self.Reps = []
		self.Rest = []

	def check_params(self):
		print(self.Name + " Week")
		print("Intensity = " + self.Intensity)
		print("Sets = " + self.Sets)
		print("Reps = " + self.Reps)
		print("Rest = " + self.Rest)

wave = Wave()
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


# print(week.Name,week.Intensity,week.Sets,week.Reps,week.Rest)
week.check_params()





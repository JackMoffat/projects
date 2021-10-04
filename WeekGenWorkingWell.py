import csv
from collections import defaultdict

#Importing the sheet with the parameter dictionaries
import MainParamsByWeek

class Wave:
	"""docstring?"""

	def __init__(self,name):

		self.Wavename = name
	
	def add_weeks(self):
	#-----adds named weeks to list-----#
		x = MainParamsByWeek
		weeks = []
		for i in dir(x):
			if i[0].isalpha():
				weeks.append(i) 
		Wave.weeks = weeks

		for i in range(len(self.weeks)):
			key = 'week' + str(i) #relic of initially having all weeks to come defined as week0,week1 etc
			val = Wave.weeks[i]
			setattr(self,val,Week(self,val))
#-------the combination of these sets will have to be different. Like, outside of the class definitions



class Week(Wave):
	"""docstring?"""

	def __init__(self,Wave,weekname): #add a weekname here and pass in somehow?

		self.Wavename = Wave.Wavename
		self.Weekname = weekname
		self.Intensity = []
		self.Sets = []
		self.Reps = []
		self.Rest = []
		self.rtf = []

	# 0-intensity,1-sets,2-reps,3-rest,4-rir
	def week_update(self):
		week_name = eval("MainParamsByWeek." + self.Weekname)

		if self.Wavename in week_name: 
			params = week_name[self.Wavename]
			self.Intensity = params[0]
			self.Sets = params[1]
			self.Reps = params[2]
			self.Rest = params[3]
			self.rtf = params[4]
		else:
			print("something's busted")

	def check_params(self):
		print("Wave = "+ self.Wavename)
		print("Week = "+ self.Weekname)
		print("Intensity = ", self.Intensity)
		print("Sets = ", self.Sets)
		print("Reps = ", self.Reps)
		print("Rest = ", self.Rest)
		print("Reps in reserve = ", self.rtf)

#---creating the wave and week----#
Fives = Wave('5s')

Fives.add_weeks()

Fives.Accumulation.week_update()
Fives.Accumulation.check_params()

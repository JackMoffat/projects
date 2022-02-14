import csv
from collections import defaultdict

#Importing the sheet with the parameter dictionaries
#This part, and references to MainParamsByWeek especially as string must be recoded to allow for modularity of input name
import MainParamsByWeek

class Wave:
	"""docstring?"""
	def __init__(self,name):

		self.Wavename = name
	
	def add_weeks(self):
	#-----adds week names to list-----#
		x = MainParamsByWeek
		Wave.weeks = []
		for i in dir(x):
			if i[0].isalpha():
				Wave.weeks.append(i) 
	#----This is where the weeks get built with the specific names-----#
		for i in range(len(self.weeks)):
			wkname = Wave.weeks[i]
			setattr(self,wkname,Week(self,wkname))

	#----perform rolling week_update on all weeks----#
	def update_all_weeks(self):
		for i in range(len(self.weeks)):
			x = getattr(self,Wave.weeks[i]) # "x = each week"
			x.week_update()

	def add_and_update(self):
		"""Because why not do both"""

		Wave.add_weeks(self)
		Wave.update_all_weeks(self)



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

#Fives.add_weeks()
#Fives.update_all_weeks()


Fives.add_and_update()

Fives.Accumulation.check_params()
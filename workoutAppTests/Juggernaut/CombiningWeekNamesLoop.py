import csv
from collections import defaultdict

#Importing the sheet with the parameter dictionaries
import MainParamsByWeek

#Current question is on how to define, or pre define, the weeks based off the names pulled in from weekgen
## - moving it to general scale, and taking myself out of defining weeks
class Wave:

	def __init__(self,name):

		self.Wavename = name
		self.week0 = None
		self.week1 = None
		self.week2 = None
		self.week3 = None
		self.week4 = None
		self.week5 = None

	def addweek(self,obj):
		self.week0 = obj

	def weeknames(self):
	#-----adds named weeks to list-----#
		x = MainParamsByWeek
		weeks = []
		for i in dir(x):
			if i[0].isalpha():
				weeks.append(i) 
		Wave.weeks = weeks

		for i in range(len(self.weeks)):
			key = 'week' + str(i)
			val = Wave.weeks[i]
			setattr(self,key,val)
#-------the combination of these sets will have to be different. Like, outside of the class definitions



class Week(Wave):

	def __init__(self,Wave):

		self.Wavename = Wave.Wavename
		self.Weekname = ''
		self.Intensity = []
		self.Sets = []
		self.Reps = []
		self.Rest = []
		self.rtf = []

	# 0-intensity,1-sets,2-reps,3-rest,4-rir
	def week_update(self,week_name):
		week_name = eval("MainParamsByWeek." + week_name)

		if self.Wavename in week_name:
			self.Weekname = week_name['name']
			params = week_name[Fives.Wavename]
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


Fives.weeknames()
print(Fives.weeks)
print(Fives.week0)
print(Fives.week1)
print(Fives.week2)

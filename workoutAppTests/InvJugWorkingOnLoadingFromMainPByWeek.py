import csv
from collections import defaultdict

#Importing the sheet with the parameter dictionaries
import MainParamsByWeek

class Wave:

	def __init__(self,name):

		self.Wavename = name


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

		if Fives.Wavename in week_name:
			x = MainParamsByWeek.Accumulation
			Accum.Weekname = x['name']
			x_params = x[Fives.Wavename]
			Accum.Intensity = x_params[0]
			Accum.Sets = x_params[1]
			Accum.Reps = x_params[2]
			Accum.Rest = x_params[3]
			Accum.rtf = x_params[4]

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
Accum = Week(Fives)

Accum.week_update('Accumulation')
#Accum.check_params()


print(Fives)
#print(MainParamsByWeek.Accumulation)
# week_name = 'Accumulation'
# print(eval("MainParamsByWeek."+ week_name))
#Ok so right before the end, I tried to indent the class week to inside the class wave but was not successfull yet in making that work. will now try

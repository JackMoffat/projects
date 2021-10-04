import csv
from collections import defaultdict

#Importing the sheet with the parameter dictionaries
#This part, and references to MainParamsByWeek especially as string must be recoded to allow for modularity of input name
import MainParamsByWeek

#---all of wave could either be change to mean mesocycle, or it could just be used in place of. for instance meso_dir-#

class Macrocycle:
	"""This currently is made to contain the whole thing, such that it is easier to generate its components"""
	def __init__(self):
		pass

	def meso_dir(self):
# this appears to have the capacity to autocreate the waves no?
# would a class attribute be updated if its attribute were updated in one object?
# this below allows for....
		mesos = []
		for i in dir(MainParamsByWeek):
			if i[0].isalpha():
				x = getattr(MainParamsByWeek,i)
				for i in x.keys():
					if i not in mesos:
						mesos.append(i)

		for i in range(len(mesos)):
			meso_name = mesos[i]
			print(meso_name)

		print(mesos)

class Wave:
	"""docstring?"""
	def __init__(self,name):
		self.Wavename = name
	
	def create_weeks(self, checkparams = 'n'):
		""" 
		docstring definitely good for this one 
		"""
		x = MainParamsByWeek
		Wave.weeks = []
		for i in dir(x):
			if i[0].isalpha():
				Wave.weeks.append(i) 
	#----This is where the weeks get built with the specific names-----#
		for i in range(len(self.weeks)):
			wkname = Wave.weeks[i]
			setattr(self,wkname,Week(self,wkname)) #creates the instance attribute with the name of the week 
			x = getattr(self,Wave.weeks[i]) # retrieves this newly created instance attribute
			x.week_update() #updates said newly created instance attribute
			if checkparams == 'y':
				x.check_params()



class Week(Wave):
	"""docstring?"""

	def __init__(self,Wave,weekname): #add a weekname here and pass in somehow?

		self.Wavename = Wave.Wavename
		self.Weekname = weekname
		#----I removed all Intensity, Sets, etc parameters because they just get created upon calling first time!----#

	# 0-intensity,1-sets,2-reps,3-rest,4-rir
	def week_update(self):
		week_name = getattr(MainParamsByWeek, self.Weekname)

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

#--- so I could go up a level again here by creating a higher class or a function to create all waves at once
#---first pull the types out of the MainParams list

		#print(x)
		#trying to access individual dict values
#-Q--how to I add a user text input field into this when I hit build?



def savethisfornow():
	mesos = meso_dir()
	for i in mesos:
		print(mesos)
		meso = mesos[i]
		wkname = Wave.weeks[i]
		setattr(self,wkname,Week(self,wkname)) 

#print(Fives) # still says not defined, it never got passed properly out of loop

#0---!--Oh right, python hates numbers as start of names.--!--#
	#So, I must change the sheet format from 5s to fives for real

plan = Macrocycle()
plan.meso_dir()

plan.fives = Wave('Fives') # so here, the wave has to currently be manually made with the name of the Wave defined in the dict?
plan.threes = Wave('Threes')

plan.fives.create_weeks()
#ok, so itll have to be a "for i in plan.meso_dir (it may need to create list in a diff scope),
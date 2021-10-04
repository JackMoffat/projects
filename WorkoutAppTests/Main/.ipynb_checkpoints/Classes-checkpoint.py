import MainParamsByWeek
#---all of Meso could either be change to mean mesocycle, or it could just be used in place of. for instance meso_dir-#
class Macrocycle():
	"""This currently is made to contain the whole thing, so that it is easier to generate its components"""
	def __init__(self):
		pass
# This creates all the Mesos
	def meso_dir(self, checkparams= 'n'):

		self.mesos = []
		for i in dir(MainParamsByWeek):
			if i[0].isalpha():
				x = getattr(MainParamsByWeek,i)
				for i in x.keys():
					if i not in self.mesos:
						self.mesos.append(i)

		for i in range(len(self.mesos)):
			meso_name = self.mesos[i]
			setattr(self,meso_name,Meso(meso_name))

		for i in self.mesos:
			x = getattr(self, i)
			x.create_weeks(checkparams)

			#is this only for printing the name of the meso?
			# editing here to replace with the generation code
		#print(self.mesos)

class Meso(Macrocycle):
	"""docstring?"""
	def __init__(self,name):
		self.Mesoname = name
	
	def create_weeks(self, checkparams = 'n'):
		""" 
		docstring definitely good for this one 
		"""
		x = MainParamsByWeek
		Meso.weeks = [] #Why is this done with Meso.weeks instead of self.week?
		for i in dir(x):
			if i[0].isalpha():
				Meso.weeks.append(i) 
	#----This is where the weeks get built with the specific names-----#
		for i in range(len(self.weeks)):
			wkname = Meso.weeks[i]
			#---try fixing week here----#
			setattr(self,wkname,Week(self,wkname)) #creates the instance attribute with the name of the week 
			x = getattr(self,Meso.weeks[i]) # retrieves this newly created instance attribute

			x.week_update() #updates said newly created instance attribute
			if checkparams == 'y':
				x.check_params()

class Week(Meso):
	"""docstring?"""

	def __init__(self,Meso,weekname): #add a weekname here and pass in somehow?

		self.Mesoname = Meso.Mesoname
		self.Weekname = weekname
		#----I removed all Intensity, Sets, etc parameters because they just get created upon calling first time!----#

	

	def name_fix(self, name, tag_splitter):
		# name_fix will split name at instances of tag_splitter, remove the first value of the resulting list,
		# and add spaces 
		# This function is for removing Identifier or placement tags from the front of the week or phase names, 
		# if they are included, after they have serve their purpose.
		# the difference between normal split is that it only removes the indentifier tag, then reassembles the rest of it
		#----I just chopped it up a little bit so that it would work for the weeknames, it needs to be removed and made more general ex. useful on waves
		splitlist = name.split(tag_splitter)
		if len(splitlist) > 1:
			del splitlist[0]
		splitlist = ['{0} '.format(i) for i in splitlist]
		name = ''.join(splitlist)
		return(name)

	# 0-intensity,1-sets,2-reps,3-rest,4-rir
	# Used by create_weeks
	def week_update(self):
		week_name = getattr(MainParamsByWeek, self.Weekname)


		if self.Mesoname in week_name: 
			params = week_name[self.Mesoname]
			self.Intensity = params[0]
			self.Sets = params[1]
			self.Reps = params[2]
			self.Rest = params[3]
			self.rtf = params[4]

		else:
			print("something's busted")

	def check_params(self):
		print(self.Mesoname," mesocycle, ", self.Weekname)
		
		print("Intensity = ", self.Intensity)
		print("Sets = ", self.Sets)
		print("Reps = ", self.Reps)
		print("Rest = ", self.Rest)
		print("Reps in reserve = ", self.rtf)

	





#--- so I could go up a level again here by creating a higher class or a function to create all Mesos at once
#---first pull the types out of the MainParams list

		#print(x)
		#trying to access individual dict values
#-Q--how to I add a user text input field into this when I hit build?


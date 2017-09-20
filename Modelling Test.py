import random

class School():
	def __init__(self):
		self.eit_list = list()
		self.fellow_list = list()
	
	def set_schoolname(self,school):
		self.school = school


	def add_eit(self,Eit):
		eit_list.append(Eit)

	def add_fellow(self,Fellow):
		fellow_list.append(Fellow)

	def display_eits(self):
		print("EIT LIST:")
		for eit in self.eit_list:
			eit.get_eit()

	def display_fellows(self):
		print("FELLOW LIST")
		for fellow in self.fellow_list:
			fellow.get_fellow()

	def display_school_mems(self):
		self.display_fellows()
		self.display_eits()


class Person:

	def __init__(self, name, nationality):
		self.name = name
		self.nationality =nationality


class Eit(Person):
	def __init__(self, name, nationality):
		self.funfact_holder = list()
		super.__init__(name, nationality)

	# super().set_name(name, nationality)

	# super().set_nationality(self,nationality)

	def add_funfact(self,funfact):
		self.funfact = funfact
		self.funfact_holder.append(self.funfact)

	def recite_funfact(self):
		print(random.choice(self.funfact_holder()))

	def get_eit(self):
		print("EIT name: {0}\n EIT Nationality: {1} \n".format(self.name, self.nationality))



class Fellow(Person):
	def __init__(self, name, nationality):
		self.happiness_code = 0
		super.__init__(name, nationality)

	def eat(self, food):
		happiness_code += 1
		print("Happiness Level Increased!\n")

	def happiness_level(self):
		print("Happiness Level = {}\n".format(happiness_code))

	def get_fellow(self):
		print("Fellow name: {0}\n EIT Nationality: {1}\n".format(self.name, self.nationality))




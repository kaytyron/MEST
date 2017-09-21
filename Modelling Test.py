import random

class School():

	def __init__(self, school):
		self.eit_list = list()
		self.fellow_list = list()
		self.school = school


	def add_eit(self,Eit):
		self.eit_list.append(Eit)

	def add_fellow(self,Fellow):
		self.fellow_list.append(Fellow)

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
		self.nationality = nationality

	def __repr__(self):
		return "Name: {}\nNationality: {}\n".format(self.name, self.nationality)


class Eit(Person):
	def __init__(self, name, nationality):
		self.funfact_holder = list()
		super().__init__(name, nationality)

	def add_funfact(self,funfact):
		self.funfact = funfact
		self.funfact_holder.append(self.funfact)

	def recite_funfact(self):
		print(random.choice(self.funfact_holder))

	def get_eit(self):
		print("EIT name: {0}\nEIT Nationality: {1} \n".format(self.name, self.nationality))



class Fellow(Person):
	fellow_number = 0

	def __init__(self, name, nationality):

		try:
			if Fellow.fellow_number > 3:
				raise Exception("We are not hiring anymore")
			else:
				self.happiness_code = 0
				super().__init__(name, nationality)
				Fellow.fellow_number += 1

		except Exception:
			print("We are not hiring anymore")



	def eat(self, food):
		self.happiness_code += 1
		print("Happiness Level Increased!\n")

	def teach(self, lesson):
		self.happiness_code -= 1
		print("Happiness Level Decreased!\n")

	def happiness_level(self):
		print("Happiness Level = {}\n".format(self.happiness_code))

	def get_fellow(self):
		print("Fellow name: {0}\nEIT Nationality: {1}\n".format(self.name, self.nationality))







Kelvin = Eit("Kelvin", "Ghanaian")
print(Kelvin)
# Andrew = Fellow("Andrew", "American")
# Miishe = Fellow("Miishe", "Ghanaian")
# Francis = Fellow ("Francis", "Ghanaian")
# Edem = Fellow("Edem", "Ghanaian")
# Pascal = Fellow("Pascal", "DRC")

# MEST = School("MEST")

# MEST = School("MEST")

# MEST.add_eit(Kelvin)
# MEST.add_fellow(Andrew)

# MEST.display_eits()
# MEST.display_fellows()



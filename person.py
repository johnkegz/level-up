#blue print
class Mammal(object):
	#constructor
	def __init__(self, age: int, height: float):
	self.height = float(height)
	self.age = int(age)
    #behaivior of a class

    def Walking(self):
        print("walking")
    def set_age(self);
        self.age = age
    @staticmethod

#object        

#instance of an object
human.walking()
#object oriented programming helps to reuse code
class Person(Mammal):
	def __init__(self, age, height):
		Mammal.__init__(self, age, height)
    def walking(self):
    	super().walking()
    	print("walking on two legs")

person = Person(10, 7.3)
person.walking()


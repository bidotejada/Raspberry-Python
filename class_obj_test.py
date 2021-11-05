class Animal():
	def __init__(self,name,color):
		self.name=name
		self.color=color

	def say_name(self):
		print(f'my name is {self.name}')

	def my_color(self):
		print(f'im {self.color}')

class Dog(Animal):
	def __init__(self,name,color,hair):
		self.hair=hair
		super().__init__(name,color)

	def set_breed(self,breed):
		self.breed=breed

dog=Dog('will','red','med')

dog.say_name()
dog.my_color()
dog.set_breed('poodle')
print(dog.breed)
print(dog,Dog,Animal,sep='\n')
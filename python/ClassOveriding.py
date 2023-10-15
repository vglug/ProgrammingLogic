class Animal:
    def make_sound(self):
        print("Some sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

my_animal = Animal()
my_dog = Dog()
my_cat = Cat()

my_animal.make_sound()  
my_dog.make_sound()     
my_cat.make_sound()     

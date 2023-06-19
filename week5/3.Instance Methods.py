# class Piglet:
#     name = "Piglet"
#     def speak(self):
#         print(f"Oink! I'm {self.name}! Oink!")

# hamlet = Piglet()
# hamlet.name = "Hamlet"
# hamlet.speak()

# class Piglet:
#     years = 0
#     def pig_years(self):
#         return self.years * 18

# piggy = Piglet()
# print(piggy.pig_years())

# piggy.years = 2
# print(piggy.pig_years())

"""OK, now it’s your turn! Have a go at writing methods for a class.
Create a Dog class with dog_years based on the Piglet class shown before (one human year is about 7 dog years)."""

# class Dog:
#   years = 0
#   def dog_years(self):
#     return self.years * 7
    
# fido=Dog()
# fido.years=3
# print(fido.dog_years())

# class Apple:
#     def __init__(self, color, flavor):
#         self.color = color
#         self. flavor = flavor

# jonagold = Apple("red", "sweet")
# print(jonagold.color)

"""Want to see this in action?
 In this code, there's a Person class that has an attribute name, which gets set when constructing the object. Fill in the blanks so that 1) when an instance of the class is created, the attribute gets set correctly, and 2) when the greeting() method is called, the greeting states the assigned name."""

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def greeting(self):
#         # Should return "hi, my name is " followed by the name of the Person.
#         return (f"Hi, my name is {self.name}") 

# # Create a new instance with a name of your choice
# John = Person("John")
# # Call the greeting method
# print(John.greeting())

# class Apple:
#     def __init__ (self, color, flavor):
#         self.color = color
#         self.flavor = flavor
#     def __str__(self):
#         return "This apple is {} and its flavor is {}". format(self.color, self.flavor)
# jonagold = Apple("red", "sweet")
# print(jonagold)

"""Remember our Person class from the last video? Let’s add a docstring to the greeting method. How about, “Outputs a message with the name of the person”."""

# class Person:
#   def __init__(self, name):
#     self.name = name
#   def greeting(self):
#     """Outputs a message with the name of the person"""
#     print("Hello! My name is {name}.".format(name=self.name)) 

# help(Person)

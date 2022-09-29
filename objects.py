#object methods
#Methods in objects are functions that belong to the object.
#create method in person class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
#inserting a function to print greeting
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("bharathi", 36)
p1.myfunc()
#modifying object properties
p1.age = 23
print(p1.age)

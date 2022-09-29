#class is a blue print to create objects
#creating a class by using keyword class
class Person:
  def __init__(self, name, age):# _init__purpose of dunder init  is to configure an object
    self.name = name             #Attributes ,properties
    self.age = age
#create object for class
#create object with name p1
p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#
class human:
  def __init__(self, job, name):
    self.job = job
    self.name = name

p2 = human("bharathi","AE")

print(p2.name)

#class method
#class method accepts cls as first arguement
#when we want to do updation w.r.s to variable we can use class method
# Class method can access and modify the class state
class car:
  base_price = 10000#class variable, this is the base price of car in 2022
  def __init__(self,windows,doors,power): #creating initialization cinstructor
    self.windows = windows #instance variables
    self.doors = doors
    self.power = power
  def what_base_price(self): #here created other function
    print("the base price is {}".format(self.base_price))
  @classmethod#I need to add inflation on base price by 10% in 2023
  def revise_base_price(cls,inflation):
    cls.base_price = cls.base_price+cls.base_price*inflation#to know what is the 10% of value

  #@staticmethod #no need to pas any parameters,quite faster than other methods
  #def check_year():
   # if now.year == 2022:
    #  return true
    #else:
     # return false

car1 = car(4,5,2000)
print(car1.base_price) #it prints the base price
car1.revise_base_price(0.10) #here updating the inflation to 10%
print(car1.base_price)#it prints the updated base price by 10%
#print(car1.check_year())
#static method
#static method can be called without an object for that class.
#for ststic method we do not provide any parameters as self,and cls
#as soon as cls loaded the firstbthing is get initializwd that is static method





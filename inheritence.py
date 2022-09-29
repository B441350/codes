#class that inherits all the methods and properties from another class
#creating a class named person with properties fname and lname
class Person:
  def __init__(self, fname, lname): #constructor it initializes the objects
    self.firstname = fname
    self.lastname = lname

  def printname(self): #possible to create methods as per requirements
    print(self.firstname, self.lastname)
#here using the Person class to create an object, and then execute the printname method:

x = Person("bharathi", "bharu")
x.printname()
#create child class
#send the parent class as a parameter while creating child class
class student(Person):
    pass  # when we dont want add any other properties and methods to class we use pass keyword
x = student("java","basics")
x.printname()
###############################################################################

###############################################################################
#single inheritence
# single inheritance

# Base class
class Parent:
    def func1(self):
        print("bharathi")

#child class
class Child(Parent):
    def func2(self):
        print("badikala")

object = Child()
object.func1()
object.func2()
#########################################################################

##########################################################################
#multiple inheritence
#class derived from more than one class
class Parent: #base class1
    def func1(self):
        print("function 1")

class Parent2: #base class 2
    def func2(self):
        print("function 2")
#creating child class
class Child(Parent, Parent2):
    def func3(self):
        print("function 3")
#creating objects for child class and access methods and properties of base classes through it
ob = Child() #object for child class
ob.func1()
ob.func2()
ob.func3()
####################################################################################

##################################################################################33
#multi level inheritence
class A:  #craeting parent class(grandmother)
    def demo (self):
        print(" From class A")

class B(A): #it becomes class for above class(mother)
    def demo(self):
        print(" From class B")

class C(A): #create another class(me)
    def demo(self):
        print(" From class C")

class D(C,B): #(another class created treated it as my (daughter)
    def check(self):
        print("This is an example showing Method Resolution order")
#craete object for D class
#we can inherits all the properties from above clases through D class
obj = D()
obj.demo()
obj.check()
## Python program to demonstrate
# overriding in multiple inheritance
##########################################################################

#########################################################################
# Defining parent class 1
class Parent1():

	# Parent's show method
	def show(self):
		print("Inside Parent1")

# Defining Parent class 2
class Parent2():

	# Parent's show method
	def display(self):
		print("Inside Parent2")


# Defining child class
class Child(Parent1, Parent2):

	# Child's show method
	def show(self):
		print("Inside Child")


# Driver's code
obj = Child()

obj.show()
obj.display()


#############################################################################
## Python program to demonstrate
# calling the parent's class method
# inside the overridden method using
# super()
class A:
    def show(self):
        print("inside A class")
class B(A):
    def show(self): #this child cls show methhod overrides the parent cls show mwthod,by
                    # using super function we can able to call the parent class methods
        super().show() #use super function to call the  to call superclass fucntion
        print("bharathi inside B cls")
obje = B()
obje.show()
#######################################################################################

#####################################################################################
#multi level inheritence
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name,self.age)
class person1(person):
    def __init__(self,name):
        self.name=name
    def printnam(self):
        print(self.name)

class person2(person1):
    def __init__(self,name,age,cls):
        self.name = name
        self.age = age
        self.cls = cls
    def printcls(self):
        print(self.cls)

ob = person2('bharathi',23,12)
ob.printname()
ob.printcls()
ob.printnam()
#################################################################

##################################################################
#multi level inheritence with override method
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printname(self):
        print("bharathi")
    def printage(self):
        print("age is",23)
class person1(person):
    def __init__(self,name,age):
        self.name=name
        self.age= age
    def printnam(self):
        print("nani")

class person2(person1):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printname(self):
        print("puppy")
    def printage(self):
        print("age is",12)

ob = person2("bharathi",23)
ob.printage()
ob.printname()






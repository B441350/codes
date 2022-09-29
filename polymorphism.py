#polymorphism
#we can achieve runtime polymorphism by overriding method
#method overriding
class Parent:  #creat a base class
    def func1(self): # defining function in parent class
        print("this is parent  function")
#create child class
class Child(Parent): #here defining function in child class
    def func1(self):
        print("this is child function")  #child class function overrides the parent class
#create object for child class
ob = Child()
ob.func1()


##overriding in multiple inheritence
class person():
#craeting a class person
    def name(self): #defining name func here
        print("father")
    def display(self): #definig display function here
        print("inside person class")
class person1(): #creating another parent class with some func

    def show(self):
        print("mother")
    def name(self):
        print("inside person1 class")
class child(person,person1): #creating child class

    def display(self):
        print("child")
    def name(self):
        print("inside child class")
#Creating objectt

obj = child() #creating object for child class
obj.display() #when we call the display function here wtever the display function in person class
# will get override by child display function
obj.name()

#example code for inheritence
class person1: #craete a class named person1 with fname .lname properties and printname method

    def __init__(self, fname , lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = person1("dhoni","bharu")
x.printname() #executes the printname method

#crrate child classs
class person1: #craete a class named person1 with fname .lname properties and printname method

    def __init__(self, fname , lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
class student(person1): #now this student class has the same properties and methods as person1 class
    pass #pass is used wn we dont want to add any other properties and methods to class

x = student("dhoni","badikala") #create objet for child class and acess the parents printname method
x.printname()

#using super () function here

class person1: #craete a class named person1 with fname .lname properties and printname method

    def __init__(self, fname , lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person1): #when we add __init__()func, child class will no longer inherits the parents funct
    def __init__(self, fname, lname): #childs __init__funct()overrides the inheritence of parents __init__func
        super().__init__(fname,lname) #bu using super() it automatically inhrits the methods and properties from its parents

x = student("badikala","bharathi")
x.printname()

##################add graduation year to student class
class person1: #craete a class named person1 with fname .lname properties and printname method

    def __init__(self, fname , lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person1):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2021  # adding graduationyear method to student class

    def welcome(self): #add welcome method to student class
        print("welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)
x = student("badikala","bharathi")
x.welcome()






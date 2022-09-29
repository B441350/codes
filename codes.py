#overriding in multiple inheritence
class person():

    def name(self):
        print("father")
    def display(self):
        print("inside person class")
class person1():

    def show(self):
        print("mother")
    def name(self):
        print("inside person1 class")
class child(person,person1):

    def display(self):
        print("child")
    def name(self):
        print("inside child class")
#Creating objectt

obj = child()
obj.display()
obj.name()



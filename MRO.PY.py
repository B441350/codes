#method resolution order defines the order in which the base classes are
# searched when executing a method.
class AB:
    def myname(self):                #here i am performing the multi level inheritence
        print("this is in class AB") #it define sthe order in which base class are searched
class BC(AB):
    def myname(self):
        print("this us in class BC")    #AB-->BC==>EF
                                        #AB-->DE==>EF
class DE(AB):
    def myname(self):
        print("in class DE")
class EF(BC,DE):
    def muname(self):
        print("in class EF")

ob = EF()
ob.myname() #IT PRINTS the bc myname function

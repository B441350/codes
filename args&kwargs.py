#posiytional and keyword argvs
def person(name,age = 28): # if we mention values here it is default arguements
    print(name)
    print(age)

person('navin',18) #actual argumrnts
person(name ='navin',age = 18)#keyword arguements
#it allows us to pass the variable length of
# keyword arguments to the function.

#####################################################

########################################################
#keyword arguements,kwyword args perform the dictionary operations
def intro(**data): #def func intro ** data as a parameter

    # print("type of arguement,,",type(data))
    for data in data.items():
        print("{}".format(data))

#pssing two different lengths of keyword arguements
intro(fname ="badikala",lname='bharathi',age=23,location='bglr')
intro(job='AE',company='volvo',package=7.5)

#############################################################

##############################################################
def myfunc(*args,**kwargs):
    print("args:",args)
    print("kwarhs",kwargs)
#here we can pass mutilple args and kwargs
myfunc('bhar','nani','are',fname ='badikala',lname='bharathi')

##################################################################
##################################################################
# Using *args to set values of object
class person:
    def __init__(self,*args):
        self.age = args[0]##access args index
        self.name = args[1]
        #create objects for person class
ob = person(23,'bharu')
ob1 = person(20,'nani')
ob2 = person(30,'puppy')

print(ob.name,ob.age)
print(ob2.age)

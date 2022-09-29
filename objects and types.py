# Python id() function example
#id function returns the unique integer id for an object
# Calling function
val = id("Javatpoint") # string object
val2 = id(1200) # integer object
val3 = id([25,336,95,236,92,3225]) # List object
#  result
print(val)
print(val2)
print(val3)
if val == val2:
    print("true")
else:
    print("false")

#augmented assignment:
#update the variable and save to sasme memory
a = 5
a += 3
print(a)
#mutable objects
r = [2,4,8,9]
s = r
print(s)
#value and identity equality
r = [2,3,4]
s = [2,3,4]
if r == s:
    print("true")
else:
    print("false")
#arguement passing
m = [2,4,5,6] #create a list
def modify(k): #def function modify
    k.append(8)
    print("k =",k)
modify(m)
print(m)
#replacing the arguement value
#functions arguements are transferred using pass_by object_reference
#reference to objects are copied
f = [3,5,7,1,]
def replace(g):
    g = [2,9,4]
    print("g =",g)
replace(f)

#function arguements
#def is a statement executed at runtime
#default argv are evaluated when def is executed

#mutable default values
#create an empty list as an default argv
def add_spam(menu=[]):
    menu.append("spam")#when we append spam to the defAult value of the empty,
    # we get just spam
    return menu
breakfast = ['eggs','dgosa']#
add_spam(breakfast)
lunch= ['beans']
add_spam(lunch)

#immutable default values
def add_spam(menu=none):
    if menu is None:
        menu=[]
    menu.append('spam')
    return menu
add_spam()
#we call the functions repeatedly with no argv
           #we get the same menu,one order of spam each time











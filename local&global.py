#variable declared outside of the function called global var
#global variable can be accessed inside or outside of the function.

x = "global" #here created x as a global var
#defined foo()to print global varaible
def foo():
    x="local"
    print(x)

#call the foo() it print the x
foo()
print(x)
###############################################################
# Modifying Global Variable From Inside the Function
c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In outside:", c)
###################################################
#local and global variables
x = "global " #global var

def foo():
    global x
    y = "local"  # here defining local var  in foo
    x = x * 2 # here modifying the global variable
    print(x)
    print(y)

foo() #After calling the foo(), the value of x becomes global global because we used the x * 2

#global and local var with same names
x = 5  #globa var

def foo():
    x = 10   #local var defining in foo()
    print("local x:", x)


foo()
print("global x:", x)
#We get a different result when we prin
#due to global var declared outside the foo() &local var declared inside foo()

# Python program to show how global variables and local variables are different
var = 56
# Creating a function
def addition():
    var1 = 7
    c = var + var1
    print("In local scope: ", var1)
    print("Adding a global scope and a local scope variable: ", c)
addition()
print("In global scope: ", var)



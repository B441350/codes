#exception handling
def reciprocal(num1):
 try:
     reci = 1 /num1
 except: #it executes only when we have errors
     print("we can not divide by zero")
 else: #it executes when there is no errors
     print (reci)

 finally: #it will executes irrespective of errors
    print("something went wrong")

#calling function by passing variables
reciprocal(4)
reciprocal(0)

#multiple excepts blocks
try:
    name = 'Bob'
    name += 5
except NameError as ne:
    # Code to handle NameError
    print("nameerroe")
    print(ne)
except TypeError as te:
    # Code to handle TypeError
    print("typeerror")
    print(te)
else:
    print(name)
finally: #can be useful to close objects and clean up resources.
    print("something went wrong")

#exceptions and control flow
Digit_map = {
    'zero' : '0',
    'one'  : '1',
    'two'  : '2',
}
def converter(s): # defining afunction called convert here
    number =''
    for token in s:
        number += Digit_map[token]
    x = int(number)#converting string to integer
    return x #it returns the integer
###########
try:
    a=5
    b='0'
    print(a/b)
except:
    print('Some error occurred.')
else:
    print("print program")

####
#context manager is object designed to be used in a witrh statement
#creating context managers using classes,need to ensure that the class has 2 methods ,enter & exit methods
#program to create context manager
# class context_manager():
#     def __init__(self):
#         print("init method called")
#     def __enter__(self): #enter method
#         print("enter method called")
#     def __exit__(self):#exit method
#         print("exit method")
# with context_manager() as manager: #context manager object created
#     # that is assigned to variable after keyword
#     print('with statement block')

#exception handling
def func(a,b): #defining the function here
    try:
        c = a / b
    except:
        print("error")
    else:
        print(c)
func(2,0)
func(2,1)

###
def func(a,b):
    try:
        c = ((a+b)/(a-b))
    except:
        print("zero didvision error")
    else:
        print(c)
func(2,3)
func(2,0)









#generators functiuons that return an iterable generator object
#to create generator function will have to add yield keyword
def generator(): #creating function generator
    yield "h"
    yield "e"
    yield "l"
    yield "l"
    yield "o"

test = generator() #craete generator object for function
#use for loop to get actual values from generator func
for i in test:
    print(i)
####################################################################

#######################################################################

#normal function vs generator function

#for normal function
def normal():
    return "hello world"
#generator function using yield keyword
def generator_test():
    yield "hello world"

print(normal()) #call to nor mal function it prints string "hello world
print(generator_test()) #call for generator function it returns generator
# object to call with yield keyword
print(next(generator_test())) # if we want actual value we use next() method , it prints
# actual value in generator function
#######################################################################################

##########################################################################################
#Read actual values  from generator using list(),for-loop(), next()

#get actual values using list()
#A list is an iterable object that has its elements inside brackets
def even_numbers(n): #create generator func
    for x in range(n):
        if x % 2 == 0:
            yield x #yield represents the generator function ,
            # and returns the generators objects to call
#Using list() on a generator object will give all the values the generator holds
num = even_numbers(10) #generator object
print(list(num)) #prints the even numbers in list
##########################################################################

############################################################################
#using for loop
def even_numbers(n):
    for x in range(n):
        if x % 2 == 0:
            yield x
num = even_numbers(20)
for i in num: #accessing actual values using for loop
    print(i,end=" ")
#####################################################################

#####################################################################
#using next()method
def even_numbers(n):
    for x in range(n):
        if x % 2 == 0:
            yield x
num = even_numbers(10)
print(next(num))
####################################################################

####################################################################
#generators they are available for use only once
# If you try to use them again, it will be empty
def even_numbers(n):
    for x in range(n):
       if (x%2==0):
           yield x
num = even_numbers(10)
for i in num:
    print(i) #first calling

#when we call second time it prints empty
print("Calling the generator again: ", list(num))

##########################################################

############################################################

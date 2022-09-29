def greet(name): #definig the greet function here with anme
    """this functions greets to tye person passed in as parameter """
    print("hello" + name + "goodmorning")

greet('bharu') #call that function

#return statements
def value(num): #defininhg function here
    """This function returns the absolute
    value of the entered number"""
    if num >= 0: #if the num is >= 0 it return num else it returns -number
        return num
    else:
        return -num
print(value(2))
print(value(-4))

#callable instances
class student:
    def greet(self):
        print("hello")
    def __call__(self):#to make instance callable, we have to override the __call__ in student class
        print("hi i am a student")

std = student()  #creating object for class
print(std()) #here call the instance

#lamda function
#we can pass no.of argv but only one expression should be there
f = lambda a,b : a+b
result = f(4,5)
print(result)
#closures in functions
#local functions these are to find fiunctions in other functions


#function returns a map object(which is an iterator) of the results after
# applying the given function to each item of a given iterable
# Return double of n
def addition(n): #definig the function addition here
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

## Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

## Creating a lambda function for addition
sum_ = lambda x, y, z : x + y + z
print("Sum using lambda function is: ", sum_(4, 6, 8))





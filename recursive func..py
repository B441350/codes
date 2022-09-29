#A function is called recursive when it is called by itself
#example for factorial using the reecursive
def factorial(n):  #defining function
   if n ==0:
       result=1
   else:   #if n is not n == 0 then it performs some factorial functions here
       result = n * factorial(n-1)   #if n = 4 ,result = 4* factorial(3) = 24
   return result

x= factorial(4)
print("Factorial of 4 is: ",x)

#lambda(annoymous function)
#can take any number of arguments but should have only one expression.
#improves the readability of the code.
#This can be used for only simple functions
#lambda func is mostly used in combinations with other functions
items_cost = [999, 888, 1100, 1200, 1300, 777]
gt_thousand = filter(lambda x : x>1000, items_cost)
x=list(gt_thousand)
print("Eligible for discount: ",x)

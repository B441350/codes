# def tuple_count(input):
#
#     return input.count(1)
#
# def tuple_operation():
#
#     tuple_1 = (1,2,1,2,1,3)
#
#     print(tuple_count(tuple_1))
#
# tuple_operation()

###########################
l = [2,3,4,5,6,7]
print(l)
temp = l[1]
l[1]=l[4]
l[4]=temp
print(l)
#########to find square of given range
n = 5
for i in range(n):
    print(i * i)

########
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year
def CheckLeap(Year):
  # Checking if the given year is leap year
  if((Year % 400 == 0) or
     (Year % 100 != 0) and
     (Year % 4 == 0)):
    print(bool("Given Year is a leap Year"));
  # Else it is not a leap year
  else:
    print (("Given Year is not a leap Year"))
# Taking an input year from user
Year = int(input("Enter the number: "))
# Printing result
CheckLeap(year)

#######



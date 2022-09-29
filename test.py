amount = int(10.6)
print(amount)
hello = 'hello'
name= input("what is ur name:")
greeting = hello +"  "+ name
print(greeting)
calculating age
age = int(input("how old are you"))
decades = age/10
print("you are"+str(decades)+"decades old")

####
from operator import*
lis1 = [2,6,3]
m = 1
for i in lis1:
    m = mul(i,m)
print(m)

###########
from operator import*
lis2 = [13,28,76,2,5]
m = 1
for i in lis2:
    m = mul(i,m)
print(m)

##################
# Enter Python code here and hit the
array = [5, 3, 9, 1, 6, 12, 2, 67]

for i in range(0, len(array)):
    for j in range(i + 1, len(array)):
        if (array[i] >= array[j]):
            array[i], array[j] = array[j], array[i]

print(array)


#addition of numbers in list
lis4 = [3,9,6,45,7]
total = 0
for ele in range(0,len(lis4)):

    total = total + lis4[ele]
print("sum of elemnts in lis:",total)


#random module
import random
lis1 = [2,6,4]
print(random.choice(lis1)) #it prints the one element randmloy from lis1

#creting random integers
#random.randint() is method to get random integers in between given range
#random.randint(start,end)

r1 = random.randint(2,8)
print("random number between 2 and 8 is ;",(r1))

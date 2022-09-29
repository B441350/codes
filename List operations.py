lis = [10,20,30,40]
#extract elements from list
#by using index
print(lis[1])
print(lis[0])
print(lis[-1])
print(lis[0:2])
#up to certain element using index
#using loop to extract elements
lis1 = ["10", "11", "12", "13", "14", "15"]
print([lis1[i] for i in (1, 2, 5)])#use two different ways to create list
numbers = range(10, 16) #it creates list containing 6 elements
indices = (1, 1, 2, 1, 5) #indexes

result = [numbers[i] for i in indices]
print(result)

#list operations
abc = [2,3,4,6,7]
#append used to pass an single element
abc.append(5) #append adds elements in last to list
print(abc)
#extend is use to pass multiple elements//adds elements in last
abc.extend([7,8,9])
abc.extend([100,200])
print(abc)
#insert used to add element at particuular element
abc.insert(2,10)
print(abc)
#pop removes the last added element
abc.pop()
print(abc)
abc.remove(10)
print(abc)
#find legth of list
print(len(abc))
#concatination
l1 = [1,2,3,4]
l2 = [5,6,7,8]
print(l1 +l2)
#function definition
#adding elements in list
def calculateTotalSum(*arguments):
    totalSum = 0
    for number in arguments:
        totalSum += number
    print(totalSum)

# function call
calculateTotalSum(5, 4, 3, 2, 1)


#######################
#using while loop to find even numbers
list1 = [10, 24, 4, 45, 66, 93]
num = 0

while num < len(list1):
    if list1[num] % 2 == 0:
        print(list1[num], end=" ")
    num += 1 #updation to variable

###############
#using for loop to print eveng number in list
list1 = [11, 23, 45, 23, 64, 22, 11, 24]

# iteration
for num in list1:
    # check by writting condition
    if num % 2 == 0:
        print(num, end=" ")
#################3
#using list comprehensions to print even numbers
#even= [num for num in lis1 if lis1 % 2 == 0]
#print(even)

#Python program to print odd numbers in a List

lst=[10,21,4,45,66,93,11]
for i in lis: #iteration
    if i % 2 == 0:
        pass #it excutes nothing here
    else:
        print(i)# wtever the elements are not divisible by 2  will get printed here

#########
#square of every element of a list
#We used a for loop to iterate through every element of a list and multiply
# the element by itself to generate a square of it. Then, append to the newly generated list.
#Calculating the Average of Numbers in Python
n = int(input("Number of Elements to take average of: "))
l=[]
for i in range(1,n+1):
    element = int(input("Enter the element: "))
    l.append(element)
average = sum(l)/n
print("Average of the elements in list",round(average,2))

#Python program to reverse number:
n = int(input("Enter number: "))

reverse = 0

while (n > 0):
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print("The reverse of the number:", reverse)


#reverse the list
array = [23, 12, 5, 24, 23, 76, 86, 24, 86, 24, 75]
print("Reverse order of array is")

for i in range(len(array)-1, 0, -1):
    print(array[i])

#############################
l = [2,3,4,5,6,7]
print(l)
temp = l[0]
l[0]=l[4]
l[4]=temp
print(l)
######################################
#program to pritn even numbers from given list
num = [] #creating an empty list here
print("enter 10 numbers")
for i in range(10): # defines the length of the list with in range
    num.insert(i,int(input())) # taking inputs through user
print("even numbers")
for i in range(10): #iterating through for loop
    if num[i]%2==0: # if i is divisible by numbers and equal to 0
        # (given through user) those num will get print as even numbers
        print(num[i])

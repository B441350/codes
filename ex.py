# variable number of non keyword arguments passed

# function definition
#def calculateTotalSum(*arguments):
#    totalSum = 1
#    for number in arguments:
#        totalSum *= number
#    print(totalSum)



# function call
#calculateTotalSum(5, 4, 3, 2, 1)

#sorting of list using forloop
array = [5, 3, 9, 1, 6, 12, 2, 67]

for i in range(0, len(array)):
    for j in range(i + 1, len(array)):
        if (array[i] >= array[j]):
            array[i], array[j] = array[j], array[i]

        print(array)

#to acess index of list using loop
lis3 = [2,4,3,6,8]
for index in range(len(lis3)):
    value = lis3[index]  #index starts from zero,by using statement value =lis[index]
    # we can get the value of list

    print(index,value)

#sort string
string = "bhharathibadikala"
lis = [string[i] for i in range(0,len(string))]
lis.sort()
for i in lis:
    print(i, end=" ")
#addition of numbers in list
total =0
lis4 = [3,9,6,45,7]
for ele in range(0,len(lis4)):

    total = total + lis4[ele]
print("sum of elemnts in lis:",total)
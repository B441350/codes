def fahrenhit(c):
    return(c*5/9)+32
def celsius(f):
    return(f-32) * 5/9
i = 0
while i == 0:
    print("1.print celsius to fahrenhit")
    print("1.print fahrenhit to celsius")
    choice = int(input("enter ur choice="))
    if (choice==1):
        c = int(input("enter the celsius temperature="))
        print("the fahrenhit temp=",fahrenhit(c))
    if (choice==2):
        f = int(input("enter the fahrenhit temp="))
        print("tha celsius temp=",celsius(f))
        break

#program to count the no.of words and letters in pyhton
#initializing string
test_string = "hello this is bharathi new to volvo"
print(len(test_string))
# to count words in string
res = test_string.count(" ") + 1

# printing result
print("The number of words in string are : " + str(res))

def fun(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

list1 = [2,3,5]
list2 = [4,7,12,8]
list3 = [2,9]
print(fun(list1))
print(fun(list2))
print(fun(list3))


#Print characters from a string that are present at an even index number

string = "hello this is bharathi"

even_chars = []

for i in range(len(string)): #iterating through the characters one  by one
    if i % 2 == 0: #checks the current index value and append it to even_chars
        even_chars.append(string[i])

print('Even characters: {}'.format(even_chars))

#reverse the number
num = 123456
print(str(num)[::-1]) # it iterates the complete string and -1 indicates the end value

#######################
####################















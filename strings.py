#create a list
thislist = ["apple", "banana", "cherry"]
print(thislist)
#list allows the duplicate values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#accessing string characters by indexing
#Accessing string characters in Python
str = 'bharathi'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])
#concatination of strings
# Python String Operations
str1 = 'Hello123 '
str2 ='World!'
print(str1 + str2) #concatination of string
print(str1.isalnum()) # if string have any alpha numerics it prints true
print(str1.isalnum() and str2.isalpha()) # if both are true then only we can get true if we use and logic

#convert string to list in pyhton
str = "analytics vidhya"
print(str.split())



## Python program to check if the given string is a palindrome

# Creating a string
sequence = 'abjucujba'
# Reversing the string
reverse = sequence[::-1]

# Checking if the string is a palindrome
if reverse == sequence:
    print("The sequence is a palindrome")
else:
    print("The sequence is not a palindrome")

#program that removes vowels from a string
###########################################
str = "bharathibadikala"
#here i created the list of vowels
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#Then initializes characters, one by one to new_str and the only characters
# does not present in any of 10 vowels available in the list
new_str = "" # the variable new_str holds the string entered by user, but without any vowels
for c in str:

    if c not in vowels:
        new_str = new_str + c
print("with vowels= ",str)
str = new_str #So, initialized its value to str  the value of str gets
# printed as string without vowels
print("without vowels= ",str)
#################################################################3

#reverse string
#creating a string
str9 = "bharathi badikala"
print(len(str9))
len(str9)-1 # here we ae pointing i to -1 means end the string
for i in range(len(str9)-1,0,-1): # starts itersting from -1 and stops at 0
    print(str9[i],end="")
##############################################################
###############################################################3
#reverse the string using slicing operator
str = "bharathibadikala"
print(str[::-1])

###################################################################
#####################################################################
#program to swap case the letters

# s = "bhAraThi"
def swap_case():
    s = "bhAraThi"
    output='' # creating output array leave it empty it holds the letters return by output
    for char in s:
        # print(char)
        if char.islower() == True: # if this condition satiesfies it adds
                                   # upper case letters to output
            output += (char.upper())
        elif char.isupper() == True: #if this condition satiesfies it adds
                                   # lower case letters to output
            output +=(char.lower())
        else:                        # else it executes thihs condition
            output = output+char
    return output
print(swap_case()) # calling the function to get output

###############################################################################

###############################################################################
#program to count vowels in string
str = "bharathi badikala"
count = 0 # initializing count to 0
for i in str: # it checks letters in string with this condition if its true id adds to count
    if (i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i=='A'or i=='E' or i=='I' or i=='O' or i=='U'):
        count  = count + 1
print(count)

###########################################################333333333333333

#############################################################################
#program to count vowels and constants
string = "bharathi badikala"
vowels = 0
constants = 0
for i in string:
    if i in('a','e','i','o','u','A','E','I','O','U'):
        vowels = vowels + 1
    elif i.isalpha():
        constants += 1
print("vowels =",vowels)
print("constants = ",constants)
###############################################################################
##################################################################################
def func(s1,s2):
    print(s1.replace(s2,''))
s1 = input("enter the string")
s2 = input("enter the char to remove")
func(s1,s2)
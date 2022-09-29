
# Example of pass, break, continue
# pass: does nothing. useful when testing something or when that code block is not required
# break: terminates the current loop and resumes execution at the next statement
# continue: returns the control to the beginning of the loop

#example for break statement
my_list = ['Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru']
i = 0 #The loop execution starts.
#If the loop condition is true, it will executes
while True:
    print(my_list[i])
    if (my_list[i] == 'Guru'):
        print('Found the name Guru')
#once met with condition,it go to end of the loop
        break
        print('After break statement')
    i += 1

print('After while-loop exit')

#example for continue statement
number = 10
while number > 0: #condition
   number = number -1  #it executes until the current variable = 0
   if number == 5:
      continue     #continues the execution
   print ('Current variable value :', number)
print ("Good bye!")

#example for pass statement
#pass statement can be used in for loop when user doesn’t know what to code inside the loop
a = 10
b = 20

if (a < b):
    pass #does nothing
else:
    print("b<a")

#break statement
my_list = ['guru','nani','bharu'] #creating alist with names
for i in range(len(my_list)):
    print(my_list[i])
    if my_list[i] == 'guru':
        print("name found guru")
        break
        print("loop terminates")
# Python program to check if a number is prime or not

# Declaring a variable
n = 37
if n == 2:
    print("2 is a prime number")

if n != 1:
    for i in range(2, n):
        if n % i == 0:
            print("The given number is a composite number")
            break
        if i == n - 1:
            print("The given number is a prime number")
else:
    print("1 is not a prime number")








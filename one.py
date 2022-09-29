# working of AND gate

def AND(a, b):
    if a == 1 and b == 1:
        return True
    else:
        return False

def and_ops(a,b):
    return a & b

if __name__=='__main__':
    print(AND(1, 1))
    print(bool(and_ops(1,1)))

#using codiotionals(if,else,elif)
#using if statement
a = 100
b = 50
if a > b: # if condition satisfies it will print a is greater
    print("a is greater")

#using else statement
a = 100
b = 50
if a < b:  #this condition satisfies it prints a is greater
    print ("a is greater")
else:  #if above condition is not satisfied it prints b is greater
    print("b is greater")
#using elif statement
a = 100
b = 50
if a < b:  #this condition satisfies it prints a is greater
    print ("a is greater")
elif a > b:
    print("b is greater")
else:  #if above condition is not satisfied it prints b is greater
    print("a = b")

#swap without built in function
a = int(input())
b = int(input())
a, b = b, a
print(a,b)

###########
fer = float(input('enter the farenhit temp'))
cel = (fer - 32) * 5/9 #celsius = (fer - 32) * 5/9 equation for converting celsius to farenhit
print('celsius temperatur{0}'.format(cel))









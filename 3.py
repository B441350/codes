def mul(*list):
    result = 1
    for x in list:
        result = result * x
    return result
print(mul(40,50,60))
print(mul(10,20,30))

#############
def add(a,b,c = 3):
    return(a+b+c)
print(add(b = 4,a = 2))

##################
def add(*args):
    print(args,type(args))
print(add(2,3,4,5))
##############
def add(*arguements):
    result = 0
    for i in arguements:
        result += i
    return result
print(add(1,2,3,4))
print(add(1,2,3,4,5,6,6))
#####################3
str = "bharathi badikala"
print(len(str))
len(str)-1
for x in range(len(str)-1,0,-1):
    print(str[x],end="")

###############
#kwargvs
def total_fruits(**fruits):
    total = 0
    for amount in fruits.values():
        total += amount
    return total
print(total_fruits(mango=5,banana=6,guava=10))
print(total_fruits(mango=5,banana=6,guava=10,jshdbf=90))

#####################
#positional and keyword arguements
def func(*args, **kwargs):
    print(args,kwargs)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])

print(func(3,4,6,8,9, a=6,b=7,c=8))






#########
# r = 234
# print(bin(r))
# g = 4
# print(bin(g))
# print(r ^ g)
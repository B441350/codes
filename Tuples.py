

#creat tuple
mytuple = ("apple", "banana", "cherry")
print(mytuple)
#tuple items are ordered .uncheangable,allow duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))
#Tuple items can be of any data type
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
#accessing elements
print(tuple1[1])
#range of indexes
print(thistuple[2:4])
print(thistuple[2:])

#concatination
t1 = (20,15,"bharu")
t2 = (30,10,25)
print(t2 +t1)
print(len(t1 + t2))

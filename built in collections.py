#tuples
t = ('norway',4,98,8,3)#creating tuple,it ballows multiple data types
print(t)
#accesiing by index values
print(t[0])
print(len(t))
#iterate using for loop
for item in t:
    print(item)
#*used to repeat the values
print(t*3)

#nested tuples
a = ((10,20),(30,40),(50,60))
print(a[2])
print(type(a))#type func used to define data type

#create tuple with existing collection object ,
#we can usse tuple constructor


#strings
#string formatting
str = "the age of {0}is {1}".format('jim',32)
#field names 0 and 1 are matched with positional argv
print(str)


#f string
value = 4 * 20
#use f string to insert value into string
#f - string evaluates it as normal pyhton expression
#instaed of needing to pass value into a method
print(f'the value is {value}')#inserting rsult into reesulting string


#ranges
#range(start,stop)
range(0,5)
for i in range(5):
    print(i)


#enumerate func()
#it constructs an iterable of (index,value)tuples around
# another iterable object
t = [2,3,4,5,6,10.00]
for p in enumerate(t):
    print(p)







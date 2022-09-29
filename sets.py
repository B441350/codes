
#string created
str = 'bharathi'
print('str = ', str)
#accessing
#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])
#concatination of strings
# Python String Operations
str1 = 'Hello'
str2 ='World!'

# using + (concatination)
print('str1 + str2 = ', str1 + str2)
print(len("str1 + str2"))

#create strings with triple quotes
#we can write multiple lines using thrible quotes
my = "hello welcome to world" \
     "this is bharathi" \
     " hc hjc hdcbhd"
print(my)

#check string
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#set are unordered collection of unique eleemnts
#sets are mutable
p = {3,5,7,8,9,10}
print(p)
s = set([2,4,5,6,7,8,9,9,8,9])
print(s)
#sets are iterable
for x in s:
    print(x)
#update the sets using update #updating s to p
p.update(s)
print(p)
p.add(30)
print(p)
#removes takes one arguement at a time
p.remove(30)
print(p)
#discard used to remove elements onlu,it takes one arguement
#it doesn't show a error when mentioned value is not in lis
p.discard(20)
print(p)
#copy method uses to copy references but not objects
l = p.copy()
print(l)
#union method used to combine two sets
blue = {'nani','puppy','lucky','kitti','kittu'}
red = {'balck','yellow','purple','lucky','pink'}
total = blue.union(red)
print(total)
#intersection will print common elements
all = blue.intersection(red)
print(all)
#differenec method finds all elemnts in first set which are not in second set
all = blue.difference(red)
print(all)
#symmetric differenceis used to printall the elements wtever in first set
#and second set but not in both
all = blue.symmetric.difference(red)
print(all)

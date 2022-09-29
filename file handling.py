#file handling
#open a file with read mode

f = open("one.py", 'r')
f = open("C:/Users/A441359/Desktop/bharathi/polymorphism.py") #specify the full path

#open a file with write mode
#it creates a new file if it does not exists,truncates the file if it exists

f = open("file.py",'w') # it creates new one, becoz there is no file with that name
f = open("file.py",'a')#open file append mode

#write something in file
f.write("bharathi")
f.close() #close file
#
f = open("file.py",'r')
#by using read function it prints , what it reads
print(f.read())
f.close()

#open the file
f = open("file.py",'r')


# #Read and write data into the file
# f = open("file.py",'r+')
# f.write("badikala")
# f.close()
#in read and write mode it overriddens the previous data
# f = open("file.py",'r')
# print(f.read())
# f.close()


#write and read data mode
f = open("file.py",'w+')
print(f.read())
f.write("hellooo")
f.close()

 #in append and read mode it  won't overrides the previous data
f = open("file.py",'a+')
f.write("  abcdef")
print(f.read())
f.close()
#with readlines we go through entire file content
with open("file.py",'r') as f:
    dat = f.readlines()
    for line in dat:
        word = line.split() # split func is used to split the words by spaces
        print(word)

#f = open("file.py",'r') as e:
#
#        dat = e.readlines()
#
#        for line in dat:
#
#            word = line.split()# split func is used to split the words by spaces
#    print(word)

#read the file
g = open('file.py', mode='r')# opening a file with read mode
g.readline()# readline is used to read the first line
print(g.readline())
print(g.readlines())#readlines used to read the entire content in file
g.seek(10)
g.close()







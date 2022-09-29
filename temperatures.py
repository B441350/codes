def fahrenhit(c): #here we are defining function fahrenhit
    return(c*5/9)+32 #formula to convert fahrenhit to celsius
def celsius(f):
    return(f-32) * 5/9 #formula to convert celsius tof ahrenhit
i = 0
while i == 0: # writting condition here
    print("1.print celsius to fahrenhit")
    print("1.print fahrenhit to celsius")
    choice = int(input("enter ur choice=")) # taking input through the user
    if (choice==1):# if we give one at choice first this statements executes
        c = int(input("enter the celsius temperature="))
        print("the fahrenhit temp=",fahrenhit(c))
    if (choice==2): ## if we give 2 at choice  this statements executes
        f = int(input("enter the fahrenhit temp="))
        print("tha celsius temp=",celsius(f))
        break # here used break to stop continuity of programming
#function copying
def welcome():
    print("welcome to volvo")
    return "welcome to volvo"
wel = welcome() # here we are copying func to another varibale wel ,
# if we delete the welcome still we get the ouput
welcome()#
print(wel)

#closures
def main_welcome(): #parent funtion
    #wtever varibles we declare in parent function those are accessable in sub function
    msg="hello"
    def sub_welcome():#sub function in parent finction
        print("this is subfunction of main function")
        print(msg)
        print("welcome ")
    return sub_welcome()
main_welcome() # when we call parent funtion it prints inside the subclass (print(msg))


#
def main_welcome(func):

    def sub_welcome():#sub function in parent finction
        print("this is subfunction of main function")
        func()
        print("welcome ")
    return sub_welcome()

@main_welcome #decarator is where we are calling functionwith in func
def channel_name():
    print("this is decarator")

main_welcome(channel_name)
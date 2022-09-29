# #Introspection is an ability to determine the type of an object at runtime.
# ab = [1,2,3,4,5,6]
# print(dir(ab)) #dir returns the methods and attributes  associated with taht object
# print(id(ab))
# str = "bharathi"
# print(repr(str))

class Employee:

    # Initializing
    def __init__(self):
        print('Employee created')

    # Calling destructor
    def __del__(self):
        print("Destructor called")

def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')

########################
class parent1:
    def __init__(self): #constructor
        print("constructor")
    def __del__(self):#destructor
        print("calling destructor")
obj=parent1()
del obj # by using this del keyword we can delete all object instances

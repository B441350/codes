class abcd:
    pass
a = abcd()
print(a)
print(type(a))
#create class using type,#create class dynamically
b = type ('python',(),{'x':10})
ob = b()
ob.x

#create a custom meta class(program)
class meta(type): #type is used to create all classes behind the scenes
    pass
#customize the class creation process by passing meta class keyword in class definition
class metal(metaclass=meta):# this is shows that __main__meta means instance of meta class
    pass
print(type(metal))
print(type(meta))


#another program using __init__()
class metatwo(type):

    def __init__(self,name,age,rela):
        print("this")
        return None #init method returns none

class meta3(metaclass=metatwo):
    pass

ob = meta3() # we are initializing the object here we get this will print here

############
class metal(type):
    def __new__init(cls,name,age,rela):  #new is used when one wnats to define dict,or
        # base tuples before the clsss is created
        print(rela)
        return type(name,age,rela)#return value of new is instance of cls

class meta4(metaclass=metal):
    x = 0
    y = 10

a = meta4()
print(a.y)



#program to create custom meta classes
class mymeta(type): # if meta class is given it is not an instance of type(),
# it is directly used as the metaclass
    pass
class myclass(metaclass=mymeta):
    pass
class subclass(myclass):
    pass

print(type(mymeta))
print(type(myclass))
print(type(subclass))


#program ot check class is inherited from more than one base class or not
# our metaclass
class MultiBases(type):
    # overriding __new__ method
    def __new__(cls, clsname, bases, clsdict):
        # if no of base classes is greater than 1
        # raise error
        if len(bases) > 1:
            raise TypeError("Inherited multiple base classes!!!")

        # else execute __new__ method of super class, ie.
        # call __init__ of type class
        return super().__new__(cls, clsname, bases, clsdict)


# metaclass can be specified by 'metaclass' keyword argument
# now MultiBase class is used for creating classes
# this will be propagated to all subclasses of Base
class Base(metaclass=MultiBases):
    pass

# no error is raised
class A(Base):
    pass

# no error is raised
class B(Base):
    pass

# This will raise an error!
# class C(A, B):
#     pass

# If we want to change class automatically, when it is created, we use metaclasses
# For API development, we might use metaclasses
class parent:
    name = 'bharathi'
    age = 23
person = parent() #creating object for classs
name = getattr(person,'name') #getattr returns the value of named attributes of objects
print(name)
#if default value is provided
print(getattr(person,'sex','female'))
# print(getattr(person,'sex')) # here i am not providing the default value ,it shows error
######################################################################

####################################################################
###setattr program
#setattr is used to assign new values to an object or instance attribute
class nani:
    name = 'badikala'
    age = 12
d = nani()  #create object for clas
print("before name ",d.name) # printing values before using setattr
print("before age",d.age)
setattr(d,'name','krish')  #using setattr funcion we are able to assign the new values to object or instance attributes
setattr(d,'age',23) #here assigning new vaLUE TO AGE

print(d.name)
print(d.age) # it prints 23 instaed of 12 whatever the value we mention in class
#######################################################################

####################################################################
class nani:
    name = 'fly'
    age = 23
d= nani()
name = getattr(d,'name')
print(name)
setattr(d,'name','krish')
print(d.name)

###########
#descriptors used to manage attributes of different classes
# class order:
#     product = 'apple'
#     amount = 10
#
#     def set_amount(self, value):
#         if value <= 0:
#             raise valueError()
#         self.value = value
#
#     def get_amoun(self):
#         return self.amount
#
# order = order()
# print(order.amount)
# print("user ordered ",order.amount,order.product)

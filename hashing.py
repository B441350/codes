s = 'john'
print(s)
print(hash(s))
print(hash('john'))
#The hash() method returns the hash value of an object
# the object whose hash value is to be returned (integer, string, float)
text = 'bharathi badikala'
hash_value = hash(text)
print(hash_value)
#returns the hash value of an object if it has one.
# The hash value is an integer which is used to quickly
# compare dictionary keys while looking at a dictionary

#####################################################################

class b:
    def __init__(self,name,age):
        self.name = name
        self.age = age
ob = b('nani',20)
result = hash(b) #calling function ,function return the hash of this object
print(result) #prints the result

#####################################################################
class user: #creating user class
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

        # def __eq__(self, other):
        #     return self.name == other.name \
        #            and self.gender == other.gender

        def __hash__(self):
            return hash((self.name, self.gender))
        #
        # def __str__(self):
        #     return f'{self.name} {self.occupation}'

u1 = user('bharathi','female') #u1 and u2 are the instances of user class
u2 = user('nani','male')

print('hash of user1') #The hash function returns the hash value of the object
print(u1)
print('hash of user2')
print(u2)
if (u1 == u2):
    print('same user')
else:
    print("different user")
#Even though the user details are the same, the comparison yields differet objects
# In order to change it, we need to implement the __eq__ method.
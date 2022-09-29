# num = []
# print("enter 10 numbers")
# for i in range(10):
#     num.insert(i,int(input()))
# print("even numbers")
# for i in range(10):
#     if num[i]%2==0:
#         print(num[i])
# class School:
#     # class variable
#     name = 'ABC School'
#
#     @classmethod
#     def school_name(cls):
#         print('School Name is :', cls.name)
#
# # call class method
# School.school_name()


class Student:
    school_name = 'ABC School' #class variable

    def __init__(self, name, year):
        self.name = name
        self.year = year

    @classmethod #classmethod is used to change the class variable
    def change_school(cls, school_name):
        # class_name.class_variable
        cls.school_name = school_name

    # instance method
    def show(self):
        print(self.name, 'age is',self.year, 'School:', Student.school_name)
    @staticmethod
    def printdob():


jessa = Student('Jessa', 20)
print(jessa.school_name)
jessa.show()

# change school_name
Student.change_school('xyz School')
jessa.show()

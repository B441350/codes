from abc import ABC, abstractmethod
#abstract base class work
class square(ABC):

    @abstractmethod
    def color(self):
        pass

class red(square):

    def color(self):
        print("its red color")

class blue(square):

    def color(self):
        print("its blue color")
class green(square):
    def color(self):
        print("its green colour")

ob = blue()
ob.color()

ob1 = red()
ob1.color()

#abstract method implemented by its subclasses

import abc
class parent:
    def name(self):
        pass
class child(parent):
    def name(self):
        print("its child class")

print(issubclass(parent,child))

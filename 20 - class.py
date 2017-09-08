

#!/usr/bin/python

#
# 1 -  class defination
#

class Person :
    number = 0
    def __init__(self , name , age):
        self.name = name
        self.age = age
        Person.number += 1
    def showSelf(self):
        print self
        print self.__class__
    # showName function
    def showName(self):
        print "This person's name is " , self.name
    # showAge function
    def showAge(self):
        print "This person's age is " , self.age
    # show person number
    def showPersonNum(self):
        print "Person's number is " , Person.number
    # del function
    def __del__(self):
        print "the instance has been distoryed"

person =  Person('Jack' , 15)
person.showSelf()
person.showName()
person.showAge()
person.showPersonNum()

#
# 2 - get props
#
print person.name
print person.age

getattr(person , "name")
hasattr(person , 'age')
setattr(person , 'school' , 'English')
delattr(person , 'school')

# del a instance
print id(person)
del person


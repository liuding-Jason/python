

#!/usr/bin/python

#
# 1 -  class defination
#

class Person :
    # private variable
    __part = ''
    # static variable
    number = 0
    # protect variable
    _abc = ''
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


#
# 3 - decorator modal
#
def add_candle(son_fun):
    def insert_candle():
        return son_fun() + 'candles'
    return insert_candle
# make_cake = add_candle(make_cake)
@add_candle
def make_cake():
    return 'cake'
print make_cake()




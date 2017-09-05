

#!/usr/bin/python

#
# 1 - function define
#  def functionname( parameters ):
#   function_suite
#   return [expression]
#

def printStr(str):
    print str
    return

printStr('jack')

#
# 2 - python function can match the param form key
#
def showPerson(name , age =  15):
    print "name is : " , name
    print "age is : " , age
    return

showPerson('tom' , 15)
showPerson(age = 16 , name = 'jack')


#
# 3 - sinple type variable and conplex variable use
#

def showOrder(list):
    newList = list.append([1 , 2 , 3])
    return newList
mylist = [4 , 5 , 6]
showOrder(mylist)
print mylist


#
# 4 - unset length of params
#
def showParams(arg1 , *varlarge):
    print "show params : "
    print arg1
    for var in varlarge:
        print var
    return

showParams(10)
showParams(10 , 20 , 30)

#
# 5 - lambda expresion , lambda function is just a express and a nameless function
#

sum = lambda arg1 , arg2 : arg1 * arg2
print sum(10 , 20)


#
# 6 - function Variable scope , temp scope and whole scope
#

count = 0
def countAdd(count) :
    print "count will add 1 "
    count += 1
    print count
    return count

countAdd(count)
print "whole scope count is : " , count
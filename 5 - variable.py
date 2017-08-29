

#!/usr/bin/python

# this file shows different types of variable in python

# 1 - Number int long float complex

num = 12
fnum = 12.3

# delete a variable

del num

# 2 - string


str = 'abc'
str1 = "abcd"

print "string variable test"
print str
print str[0]
print str[1:2]
print str[1:]
print str * 2
print str + "test"

# 3 - list
myHobby = ['sing' , 'coding' , 'swim' , 'cook']

print "\n\n list variable test"
print myHobby
print myHobby[1]
print myHobby[1:2]
print myHobby[1:]
print myHobby * 2
print myHobby + ["5" , "6"]

# 4 - tuple
tuple = ('bob' , 125.5 , 12 , 'myLover')

print "\n\n tuple variable test"

print tuple
print tuple[0]
print tuple[1:2]
print tuple[1:]
print tuple * 2
print tuple + ("5" , "6")

# Note : list variable can be changed , nor tuple
# myHobby[1] = "new value" is ok
# tuple[1] = "new value" is error

# 5 - dictionary

dict = {}
dict['one'] = "say hello"
dict[0] = "this is second value"

newDict = {'one' : "hello" , "two" : "world" , "three" : "china"}

print '\n\n dictionary variable test'
print dict['one']
print newDict
print newDict.keys()
print newDict.values()

























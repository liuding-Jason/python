

#!/usr/bin/python

myDict = { 'name' : 'jack' , 'age' : 15 , 'school' : 'English Universite' }
myDict2 = {'name' : 'tom'}

#
# 1 - basic use
#
print myDict
print myDict['name']
print myDict['age']

#
# 2 - some operation
#
myDict['name'] = 'tom'
print myDict
# delete
del myDict['age']

#
# 3 - some APIs
#
# as for tow dict type variable , cmp could only be used to compare two dicts
print cmp(myDict , myDict2)
print len(myDict)
print str(myDict)
print type(myDict)

#
# 4 - some personal APIs
#
# show all keys in a dict
print myDict.keys()
# show all values in dict
print myDict.values()
# simple copy
print myDict.copy()
# get a value by a key , a default value could be given
print myDict.get('name'  , 'tom')
# judge whether a key is in a dict
print myDict.has_key("name")



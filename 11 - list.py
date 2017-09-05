

#!/usr/bin/python

#
#1 - list opreration
#
# refresh a variable

hobbys = ['basketball' , 'football' , 'sing']

print hobbys[1]
hobbys[1] = 'swim'
print hobbys[1]

# delete a variable
print hobbys
del hobbys[1]
print hobbys

#
# 2 - some function
#
print min(hobbys)
print max(hobbys)
print cmp(hobbys[0] , hobbys[1])
print len(hobbys)

color = ('red' , 'blue' , 'yellow')
print list(color) # change a tuple to a list

#
# 3 - some senior API
#
# append some elements at the last of hobbys
print hobbys.append(['work' , 'sleep'])
# count how many time dose a element perform in a list
print hobbys.count('sing')
# reverse a list
print hobbys.reverse()
# pop a element in a list , but note the last element in a list will be poped
print hobbys.pop()
# sort a list
print hobbys.sort()
# and so on


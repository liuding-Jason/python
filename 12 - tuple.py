
#!/usr/bin/python

myTul = ('swim' , 'eat' , 'sing' , 'check')
tiniTul = ('cook')

#
# 1 - basic use
#

print myTul
print myTul[0]
print myTul[1:]
print myTul[1:2]

#
# 2 - some operation
#
print myTul * 2
print myTul
del tiniTul

#
# 3 - some APIs
#
print max(myTul)
print min(myTul)
print cmp(myTul[1] , myTul[2])
print len(myTul)
# change a list to be a tuple
print tuple([1 , 'jack' , 'red' , 1231.56])

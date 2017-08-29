

#!/ust/bin/python

# while loop construct

count = 0

while (count <= 9):
    print 'count value :' , count
    count += 1
else:
    print "count value is more than 9"

# continue order would stop this time loop
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print i

# break order would stop all times loop

i = 1
while 1:
    print i
    i += 1
    if i > 10:
        break


# for loop construct

for letter in 'pythion':
    print 'letter is : ' , letter


books = ['history' , 'math' , 'chinese' , 'pe']
for className in books :
    print "which one is your farivate class :" , className

# anther method to loop in for construct

for index in range(len(books)) :
    print index , "- book name : " , books[index]
else:
    print "which one is your farivate!"


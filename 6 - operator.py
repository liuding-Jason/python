

#!/usr/bin/python

# operator list

# Arithmetic operator

a = 1
b = 2

print 'Arithmetic operator test'

print a + b
print a - b
print a * b
print a / b
print a % b
print a ** b
print a // b


# Comparison operator

print "Comparison operator test"

print a == b
print a != b
print a > b
print a < b
print a >= b
print a <= b
print a <> b #  be equal to !=


# Bit operator

print a&b
print a|b
print a^b
print ~a


# Logical operator - and or not

a = 10
b = 20

if (a and b):
    print "1 - a and b are true , the result is true"
else:
    print "1 - a or b are not true"

if (a or b):
    print "2 -  a or b are true , the result is true"
else:
    print "2 -  a and b are not true , the result is false"


if not (a and b):
    print "3 -  a or b are not true , the result is false"
else:
    print "3 -  a and b are true , the result is  true"


# Member operator

member1 = 15
member2 = 20
memberList = [15 , 16 , 23]

if( member1 in memberList):
    print "member1 is in memberList"
else:
    print "member1 is not in memberList"

if( member2 not in memberList ):
    print "member2 is not in memberList"
else:
    print "member2 is in memberList"


# Identity operator

id1 = 'tom'
id2 = 'jack'

if( id1 is "tom"):
    print "id1's value is tom"
else:
    print "id1's value is not tom"

if( id2 is not "tom" ):
    print "id2's value is tom"
else:
    print "id2's value is not tom"





#!/usr/bin/python

import re

#
# 1 - pattern defination by re module
# re.match(pattern, string, flags=0)
#
print( re.match('www' , 'www.baidu.com').span())


#
# 2 - re.match would match a string form the begining -- begin match
#

# from the begining matching
print( re.match('www' , 'www.baidu.com').span())
# not form begining matching
print( re.match('com' , 'www.baidu.com'))

#
# 3 - re.search would match all of the string - all match
#
print (re.search('www' , 'www.baidu.com').span())
print (re.search('com' , 'www.baidu.com').span())


#
# 4 - match group
# group(num) - show the key num result of aim line
# groups() - show all of the result of aim line
#

line = 'Cats are more smater than dogs'

matchObj = re.match(r'(.*) are (.*?) .*' , line , re.M|re.I)
if matchObj:
    print 'matchObj.group() : ' , matchObj.group()
    print 'matchObj.group(1) : ' , matchObj.group(1)
    print 'matchObj.group(2) : ' , matchObj.group(2)
else:
    print 'match fail'

#
# 5 - re.sub
#
# delete unnumber element
phone = '010-35246783'
num = re.sub(r'\D' , '' , phone)
print num





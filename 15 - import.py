
#!/usr/bin/python

#
# 1 - import a module
#
import myFun
myFun.showStr('jack')
myFun.showList([1 , 2 , 3])

#
# 3 - import some known function from a module
#
from myFun import showList , showStr
showStr('Anther methods')
showList([4 , 5 ,6])

#
# 4 - show content of a python bag
# __name__ -- the name of module
# __file__ -- the file of import
#
content = dir(myFun)
print "Bag myFun has : " , content

#
# 5 - reload a module
# reload(myFun)
#

#
# 6 -
#

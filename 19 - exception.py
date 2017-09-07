

#!/usr/bin/python

#
# 1 - try exception
# except ErrorType
#

try:
    fo = open('./foo.txt' , 'rb')
except IOError:
    print "file not exsit or dose not have right"
else:
    print "Open success , file name is " , fo.name
    fo.close()

#
# 2 - catch all exception , without any type
#
try:
    fo = open('./foo.txt' , 'rb')
except:
    print "error"
else:
    print 'file open success'
    fo.close()

#
# 3 - finally would always be  runed
#

try:
    result = 1 / 0
except:
    print 'error'
else:
    print 'else'
finally:
    print 'the finnal result '



#
# 4 - exception with params
#
def pathInt(var):
    try:
        return int(var)
    except ValueError , Argument :
        print "ValueError happened " , Argument
    finally:
        print "the params is " , var
pathInt('zfg')

#
# 5 - raise a exception
# raise [Exception [, args [, traceback]]]
#

def functionName( level ):
    if level < 1:
        raise Exception("Invalid level!", level)

functionName(0)

#
# 6 - personal exception
# RuntimeError is the base class of all exceptions
# e is used to create a instance of Networkerror
#

class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise Networkerror("Bad hostname")
except Networkerror,e:
    print e.args
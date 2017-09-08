

#!/usr/bin/python

#
# 1 - thread create -  start_new_thread
#

import thread
import time

def myThread(threadName , delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, time.ctime(time.time()))

try:
    thread.start_new_thread(myThread , ('thread-1' , 1))
    thread.start_new_thread(myThread , ('thread-2' , 2))
except:
    print "create fail"

while 1:
   pass
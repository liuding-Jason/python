
#!/usr/bin/python

# threading

import threading
import time

class myThread(threading.Thread):
    __threadNum = 0

    def __init__(self , threadId , threadName , delay):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.threadName = threadName
        self.delay = delay
        myThread.__threadNum += 1

    def run(self):
        print 'Start thread : ' ,  self.threadName
        print_time(self.threadName , self.delay , 5)
        print 'Exit thread : ' , self.threadName


def print_time(threadName , delay , maxCounter):
    count = 0
    while(count <= maxCounter):
        time.sleep(delay)
        print '%s , %s ' % (threadName , time.ctime(time.time()))
        count += 1

try:
    thread1 = myThread(1 , 'thread-1' , 1)
    thread2 = myThread(2 , 'thread-2' , 2)

    thread1.start()
    thread2.start()
except:
    print 'thread create failed'




#!/usr/bin/python

# threading

import threading
import time

class CreateThread(threading.Thread):
    threadNum = 0
    def __init__(self , threadId , delay , count):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.delay = delay
        self.count = count
        CreateThread.threadNum += 1

    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.delay , 5)
        print "Exiting " + self.name

def print_time(threadName , delay , maxCounter):
    count = 0
    while count < maxCounter:
        time.sleep(delay)
        count += 1
        print "%s : %s " % (threadName , time.ctime(time.time()))


fThread = CreateThread('thread-1' , 1 , 5)
sThread = CreateThread('thread-2' , 2 , 5)

fThread.start()
sThread.start()

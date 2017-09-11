
#!/usr/bin/python

# python server file

import socket

so = socket.socket()
host = socket.gethostname()
port = 5306

try:
    so.bind((host , port))
    so.listen(5)
except:
    print 'Server bind failed'
else:
    print 'Server bind succeed! \nhost is %s , port is %s' % (host , port)
    while 1 :
        c , add = so.accept()
        print 'Address is ' , add
        c.send('Hello Jack')
        c.close()
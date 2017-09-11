
#!/usr/bin/python

# python client server

import socket

so = socket.socket()
host = socket.gethostname()
port = 5306

so.connect((host , port))

print so.recv(1024)
so.close()

#!/usr/bin/python

# file i / o

#
# 1 - treminal input
#

rawInput = raw_input("Please input : ")
print rawInput

inputs = input('input a expression : ')
print inputs

#
# 2 - open a file
# file object = open(file_name [, access_mode][, buffering])
# file_name  access_mode -- r , rb , r+ , rb+
#

fo = open("./foo.txt", "wb")
print "file name is ", fo.name
print "file is closed  ", fo.closed
print "file mode ", fo.mode
print "add a space at the last of a file ", fo.softspace

#
# 3 - write(str) write a str in Binary to a file
#
fo.write('This is a file test in python')

#
# 4 - close a file
#
fo.close()

fo = open("./foo.txt", "rb")
#
# 5 - read(num) return nums letter
#
print fo.read(5)

fo.close()


#
# 6 - tell() tell the offset
#
fo = open('./foo.txt' , 'rb')
fo.read(5)
print 'temp offset of foo.txt is ' , fo.tell()

#
# 7 - seek() change the offset of a file
#
fo.seek(0 , 0)
str = fo.read(5)
print 'reread str is ' , str

fo.close()




#!/usr/bin/python

# os module use

import os

#
# 1 - rename a file
#
# os.rename('./foo.txt' , './fooNew.txt')


#
# 2 - remove a file
#
# os.remove("./foo.txt")


#
# 3 - make a dir
#
os.mkdir('./newdir')

#
# 4 - change a dir
#
# os.chdir("./newdir")

#
# 5 - get path
#
print os.getcwd()

#
# 6 - remove a dir
#
os.rmdir('./newdir')
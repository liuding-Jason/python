
#!/usr/bin/python
#
# extends
#

# person
class Person:
    personNum = 0

    def eat(self):
        print 'a person can eat'
    def sleep(self):
        print 'a person can sleep'

# parent
class Parent :
    mom = 'mother'
    dad = 'father'

    def __init__(self , name , age):
        self.name = name
        self.age = age
        print 'you have created your Parent'

    # show name
    def showName(self):
        print "your parent's name is " , self.name
    # show age
    def showAge(self):
        print "your parent's age is " , self.age
    def __del__(self):
        print 'your object had been destoryed'

# child
class Child(Person , Parent):
    childNum = 0
    def __init__(self , name , age , gender):
        Parent.__init__(self , name , age)
        self.gender = gender
        Child.childNum += 1
        print 'you have create a child'

    def showGender(self):
        print "your child's gender is " , self.gender

    def __del__(self):
        print 'your child object has been destoryed'


child = Child("Tom" , 16 , "boy")
child.eat()
child.showName()
child.showGender()

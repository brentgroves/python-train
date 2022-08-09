# A Sample class with init method
<!-- https://www.geeksforgeeks.org/__init__-in-python/ -->
# A Sample class with init method
class Person:
 
    # init method or constructor
    def __init__(self, name):
        self.name = name
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
# Creating different objects
p1 = Person('Nikhil')
p2 = Person('Abhinav')
p3 = Person('Anshul')
 
p1.say_hi()
p2.say_hi()
p3.say_hi()


<!-- inheritance -->
# Python program to
# demonstrate init with
# inheritance
 
class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something
 
 
class B(A):
    def __init__(self, something):
        # Calling init of parent class
        A.__init__(self, something)
        print("B init called")
        self.something = something
 
 
obj = B("Something")

A init called
B init called


# Python program to
# demonstrate init with
# inheritance
 
class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something
 
 
class B(A):
    def __init__(self, something):
        print("B init called")
        self.something = something
        # Calling init of parent class
        A.__init__(self, something)
 
 
obj = B("Something")

B init called
A init called
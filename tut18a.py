# Thu 5-5-22

#! Constructor => __init__()
class my_class:
    def __init__(self):
        print('Constructor')

a = my_class()
print('\n')

class my_class1:
    def __init__(self, b, c):
        print(b + c)

a = my_class1(4, 6)

class my_class:
    def __init__(self, b, c):
        print(b + c)
        self.b = b
        self.c = c
        
    def add(self):
        print(self.b + self.c)
        
a = my_class(4, 6)
a.add()
print('\n')
# to iniazed the data at the run time of 

class my_class:
    def __init__(self, b, c):
        print(b + c)
        self.b = b
        self.c = c
        
    def add(self):
        print(self.b + self.c)
        
    def multiply(self):
        print(self.b * self.c)
        
a = my_class(4, 6)
a.add()
a.multiply()


class my_class:
    def __init__(self, e):
        self.e = e
        
    def display(self):
        # print('MAHESH .......')
        print(self.e)

w = input('Enter the name : ')
a = my_class(w)
a.display()
print('\n')

#! __str__() => return always string only

class my_class2:
    def __str__(self):
        print('STR constructor')

c = my_class2()
print(c)
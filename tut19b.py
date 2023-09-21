
# #! Multilevel inheritance =>

# class base:
#     pass
# class derived1(base):
#     pass
# class derived2(de)



class parent:
    def f1(self):
        print('Function 1')

class child1(parent):
    def f2(self):
        print('Function 2')
class child2(child1):
    def f3(self):
        print('Function 3')

c = child2()
c.f1()
c.f2()
c.f3()
print('\n')

# c = child1()   #!ERROR
# c.f3()

class parent:
    def __init__(self):
        print('Function 1')

class child1(parent):
    def __init__(self):
        super().__init__()

        print('Function 2')
class child2(child1):
    def __init__(self):
        super().__init__()
        
        print('Function 3')

c = child2()
print('\n')

#! ==============
class parent:
    def __init__(self, name):
        print('My name is ', name)

class child1(parent):
    def __init__(self,name, degree):
        super().__init__(name)
        print('I have ', degree)

class child2(child1):
    def __init__(self, name, degree):
        super().__init__(name, degree)
        print('Now , I am working with multiple inheritance')        

c = child2('MM', 'BE')

#! Run the child class constructor
class MyClass:
    def __init__(self ,name):
        self.name = name
        print('From parent')
    
class fClass(MyClass):
    def __init__(self, name):
        print('From child', name)

c = fClass('MMMMM')
# c.f2()
print('\n')

#! super => 

class MyClass:
    def __init__(self ,name):
        self.name = name
        print('From parent')
        print(name)
    
class fClass(MyClass):
    def __init__(self, name):
        print('From child', name)
        super().__init__(name)

c = fClass('MMMMMss')

#! ====== === ====== === ====== 
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print('From parent')
        print(self.a + self.b)
        # print(c)
    
class fClass(MyClass):
    def __init__(self):
        # c = a + b
        # print('From child', c)
        super().__init__(2, 3)
        # print(c)
        
d = fClass()
print(d)


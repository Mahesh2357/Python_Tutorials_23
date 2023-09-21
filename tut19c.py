
#! === Multiple Inheritance ===
class parent1:
    def f1(self):
        print('I am a parent-1')

class parent2:
    def f2(self):
        print('I am a parent-2')

class child(parent1, parent2):
    def f3(self):
        print('I am a child')

c = child()
c.f1()
c.f2()
c.f3()
print('\n')

# *===========================
class parent1:
    def __init__(self):
        print('I am a parent-1')

class parent2:
    def __init__(self):
        print('I am a parent-2')

class child(parent1, parent2):
    def __init__(self):
        print('I am a child')

c = child()
print('\n')


# *===========================
class parent1:
    def __init__(self):
        print('I am a parent-1')

class parent2:
    def __init__(self):
        print('I am a parent-2')

class child(parent1, parent2):
    def __init__(self):
        super().__init__()
        print('I am a child')

c = child()
print('\n')


# *=== ========================
class parent1:
    def __init__(self):
        print('I am a parent-1')

class parent2:
    def __init__(self):
        print('I am a parent-2')

class child(parent1, parent2):
    def __init__(self):

        parent1().__init__()
        parent2().__init__()
        print('I am a child')

c = child()
print('\n')

class ABD:
    a = 10
print(ABD().a) #? nameless obj
c= ABD()
print(c.a)  #? named obj
print('\n')
    


# *=== ========================
class parent1:
    def __init__(self):
        print('I am a parent-1 .....')

class parent2:
    def __init__(self):
        print('I am a parent-2 .....')

class child(parent1, parent2):
    def __init__(self):
    
        parent1.__init__(self)
        parent2.__init__(self)
        print('I am a child .....')

c = child()
print('\n')
print(type(parent1))
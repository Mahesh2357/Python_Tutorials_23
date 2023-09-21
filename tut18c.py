# Inheritance

#* Single inheritance => is when each class inherits from base class
class parent_class:
    name ='MM'
    moblie = 54455454

class child_class(parent_class):
    address = 'ldfsf'

c =child_class()
print(c)
print(c.address)

p = parent_class()
print(p)
# print(p.address)


#! isinstance() => returns true if the specified object is of the specified type, otherwise false

class my_object:
    pass
c =my_object()
print(isinstance(c, my_object))
print(isinstance(c, (my_object)))
print(isinstance(c, (my_object, list)))
# print(isinstance(my_object, c))   #!ERROR
print('\n')

print(isinstance(c, int))
print(isinstance(c, str))
print(isinstance(c, float))
l = [34, 65]
print(isinstance(l, (int, list, my_object)))
print('\n')

# issubclass =>
print(issubclass(child_class, parent_class))

class MyClass:
    def f1(self):
        print('From parent')
    
class fClass(MyClass):
    def f2(self):
        print('From child')

c = fClass()
c.f1()
print('\n')

class MyClass:
    def __init__(self ,name):
        self.name = name
        print('From parent')
    
class fClass(MyClass):
    def f2(self):
        print('From child', self.name)

c = fClass('MMMMM')
c.f2()

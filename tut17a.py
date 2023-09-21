# Wed 4-5-22
#! obj - physical entity & class - logical entity

from this import d


class myclass:
    a = 13
    b = 14
    c = a+b
    print('I am a physical entity')

c = myclass()
print(c.a)
print(c.c)
print('\n')

c1 = myclass()
print(c1)

print(id(c))
print(id(c1))
print('\n')

#! Method - fun defined inside the class
#*in python, this => self

class ab:
    def fun(self):
        print('Function in between classes')

s = ab()
s.fun()
print('\n')

#? Instance variables 
#! inside class => use self
#! outside class => use obj name

class MyClass:
    a = 90
    
    def display(self):
        print(self.a)

c = MyClass()
print('The value of a : ',c.a)
c.display()
print('\n')

#! Convert loccal Data into Class level
class MyClass:
    def value(self, a, b):
        self.a = a
        self.b = b
        print(a)
        print(b)
        
    def add(self):
        print(self.a + self.b)
        
c = MyClass()
print('The value a, b : ', end='')
c.value(12, 65)
print('The value Sum : ', end='')
c.add()
print('\n')


a = int('Enter the value of a : ')
b = int('Enter the value of b : ')
class ddd:
    def value(self):
        self.a = a
        self.b = b
        
    def multi(self):
        print(self.a * self.b)

    def display(self):
        print(a, b)
w = ddd()
w.value()
print('The value a* b : ', end='')
w.multi()
w.display()
print('\n')


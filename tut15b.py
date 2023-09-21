# Fri 29-4-22

#! From folder1
from folder1.MyModule import color
print(color)

import folder1.MyModule as mm
print(mm.color)
print('\n')

mm.display()

#! call all functions at once from *
# from folder1.MyModule import * 
from folder1.MyModule import add
add(5, 1)

def greet():
    print('Good Morning')
greet()
print('\n')

def greet():
    return('Good Morning')
g = greet()
print(g)
print('\n')

#! Decorator function
#! wrapper function => wrap the greet() function
def wrapper(func):
    return func
def greet():
    return('Good Morning')
g = wrapper(greet())
print(g)
print('\n')

def a(x):
    return x
def b():
    return('MAHESH')
v = a(b())
print(v)
print('\n')


def makedecorator(func):
    def wrapper():
        print('I am a decorator function')
        func()
    return wrapper
def general_func():
    print('HELLO')
general_func()
print(general_func())
print(general_func) #! return the object of function.

def makedecorator(func):
    def wrapper():
        print('I am a decorator function')
        func()
    return wrapper
def general_func():
    print('HELLO')
    
mk = makedecorator(general_func)
print(mk)   #! object of makedecoraor

print('\n')
mk()
print('\n')


def makedecorator(func):
    def wrapper():
        print('I am a decorator function')
        func()
    return wrapper()
def general_func():
    print('HELLO')
    
mk = makedecorator(general_func)
print(mk) 
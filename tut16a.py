# Mon 2-5-22

#* decorators can modify the behavior
#! A decorator in Python is a function that takes another function as its argument, and returns yet another function .

def upperCase(func):
    def wrapper():
        data = func()
        return data.upper()
    return wrapper
@upperCase

def greet():
    return'Hello welcome to python Seed Class'
print(greet())
print('\n')

def splitCase(func):
    def wrapper():
        data = func()
        return data.split()
    return wrapper

    
def upperCase(func):
    def wrapper():
        data = func()
        return data.upper()
    return wrapper
@splitCase
@upperCase

def greet():
    return'Hello welcome to python Seed Class'
print(greet())
print('\n')

#! in python, object and value stored in Heap.

#* assigements 
# print('****** \n======')
# print('Hello, Guys...')
# print('======\n******')

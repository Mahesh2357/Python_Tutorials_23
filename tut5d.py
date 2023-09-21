#! PYTHON FUNCTIONS
#* Piece of reusable code
#* solve the perticurar task
#* call functions instead of writing code yourself

#!There are Two types of functions

#* 1. Builtin function
#? ex. print(), int(), hex(), oct(), input().

#* 2. User defined function
#? ex.

#* Round Function --
print(round(1.66, 1))
print(round(3.567, 2))

#* Reverse Function --
seq = range(10)
print(seq)
print(reversed(seq))
print(list(reversed(seq)))
print(tuple(list(reversed(seq))))
print('\n')

#* How to create User-defined function?
#! Syntax:
#* def function_name(parameter):
#*      function statement(s)
#* function_name()

def f1():
    print('I am a function')
f1()
print('I am a function with parameters')
f1()
print('\n')

#* 2nd function
def f2(name):
    print('Good doc Function', name)
f2('mmzfunc')
print('\n')

def f2(name):
    print('Good doc Function', name)
name = input('Enter the name : ')
f2(name)
print('\n')

#* note => Arguments are always the local values

def f3(x, y):
    print('Addition : ',x+y)
x = int(input('Enter the number1 : '))
y = int(input('Enter the number2 : '))
f3(x, y)

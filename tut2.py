# code- 1
#? date = 11-4-2022

#* type declaration is not required because it is dynamically type
import keyword

a = 12
print(type(a))

x = 3.44
print(type(x))

c = 'r'
print(type(c))

d = True
print(type(d))
print('\n')

#* code -2
#! python single line code
#? variable declaration single line code

eid, ename, esal = 12, 'ddd', 6000
print(eid)
print(ename)
print(esal)

#* code -3
print(keyword.kwlist)
print('\n')

#* code -4
print('it\'s')
print('how \nare \nyou')
print('welcome \nto \nthe \npython \ninterpreter')

#! indetation error
    # a = 45
print('\n')

#! Identifier in python:
#* code -5
print(5+5)
print(5.5 + 6)
print('Hello' + '14')
print(True + 5)
print(False + False)
print(True + False)    #* output => 1

a = 10
print(id(a))
b = 10
print(id(b))
a = 20
print(id(a))

print(dir(keyword))
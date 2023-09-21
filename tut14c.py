# code - 1
# date = 28-4-2022

#! python module =>
#* How to import this module in python ?

# print(help('modules'))

#? import statements =>
#! import a module using import statements and acess definitions inside them using the(.) dot operator. 
import keyword
print(keyword.kwlist)
print('\n')

#! import math
import math
print(dir(math))
print('\n')

print(math.pi)
print(math.e)
print(math.factorial(5))
print(math.sqrt(64))
print(math.sin(45))
print('\n')

import math as m
print(m.cos(64))
print(m.pow(2, 7))  #! 7 power of 2 
print(m.pow(2, 3))
print(m.pow(3, 7))
print('\n')

#! from....import statements
# we can import specific names from a module without importing them.

from math import pi, sqrt
print(pi)
print(math.pi)
print(sqrt(9))
print('\n')

#! import all names
#* import all names from a module .
from math import *
print(pi)
print(e)
print(sqrt(25))
print(pow(2, 5))

import sys
print(sys.path)
# code - 1
# date = 21-4-2022


from ast import operator
from typing import List


#* List Data Type

#! list is used to store groups of heterogeneous values.
#? list is mutable and inclosed in []


print()
l1 = []
print(l1)

l2 = list('MAHESH')
print(l2)
print('\n')

l = [324, 34, 34, 'lf', 3.45, 66, 332, 1]
for i in l:
    print(i)
print('\n')
    
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l3[0])
# print(l3[50])    #! ERROR
print(l3[3:9])
print(l3[-5])
print(l3[:])
print(l3[::3])
print(l3[::-1])
print('\n')

# enumerate function
l4 = ['Mango', 'Apple', 'Orange']
for i in enumerate(l4):
    print(i)
print('\n')


for i, j in enumerate(l4):
    print(i, ' ', j)
    
# == to operator to check data
l5 = [10, 20, 30, 40, 50]
l6 = [40, 50, 60, 70, 80]
l7 = l5
l8 = [10, 20, 30, 40, 50]
print(l5 == l7)
print(l6 == l8)
print(l6 != l8)
print('\n')

#! Q. why memory allocation of l5 and l8 id different ?
#*  Ans => list is muttable, at the run time list modify

print(id(l5))
print(id(l7))
print(id(l6))
print(id(l8))
# code - 1
# date = 26-4-2022

#* pop & push
from multiprocessing.reduction import duplicate


s5 = {34, '43',66, 101,False, True, 'gggg', (34, 54) }
print(s5)

print(s5.pop())
# print(s.push(4555))
print(s5)
print('\n')

#* Equality
s1 = { 10, 20, 30, 40}
s2 = { 50, 60, 70, 80}
s3 = s1
s4 = { 10, 20, 30, 40}

print(id(s1))
print(id(s2))
print(id(s3))
print('\n')

print(s1 is s2)
print(s2 is s3)
print(s3 is s4)
print(s3 is not s4)
print('\n')

#! unpaking data
a, b, c = {True, 'Hello', 67}
print(a, b, c)
print('\n')

s = {34, 87, 90, True, False, 23 , 'dfdfd', 'try'}
print(s)
for i in s:
    print(i)
print('\n')

for i in set('apple'):
    print(i)
print('\n')

# adding groups of values into set
# s= {1, 345, 56, 'try', True, False, 45, 232}
s = {i for i in range(1, 10+5)}
print(s)

s4 = {i for i in range(5, 50, 5)}
print(s4)

#! Q. Why we use the set() ?
#* => duplicaation is not allowed.
#* => insertion.


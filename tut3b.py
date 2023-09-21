#* code- 1
#? date = 12-4-2022


#! Arithmetic Operator

print(10+3)
print(10-3)
print(10*3)
print(10%3)
print(10/3)
print(10/3)
print(4 ** 4)
print(10//3)
print('\n')

#! Relational Operators
print(10>3)
print(10<3)
print(10==3)
print(10!=3)
print(10>=3)
print(10<=3)
print('\n')

#! Logical Operator

x = True
y = False
print(x and y)
print(x or y)
print(not x)
print(not y)
print('\n')

#! Assignment Operator
a = 5
print(a)

print('+= Operator')
a += 5
print(a)
print(a+5)

print('-= Operator')
a -= 5
print(a)

print('*= Operator')
a *= 6
print(a)

print('/= Operator')
a /= 6
print(a)

print('//= Operator')
a //= 2
print(a)

print('**= Operator')
a **= 6
print(a)

print('%= Operator')
a %= 2
print(a)
print('\n')

#! Identity Operator
a = b = 10
print(id(a))
print(id(b))
print(a is b)
print('\n')

c =15
print(a is c)
print(a is not c)
print('\n')

#! Membership Operator
l = [34, 56, 67]
print(23 in l)
print(67 in l)

name = 'ederation'
print('E' not in name)
print('\n')

t=  (45, 46, 23)
print(45 not in t)

d = {'a':34, 56:2}
print('a' in d)
print('34' in d)
print('34' not in d)
print('\n')

#! Bitwise Operator
print(10 & 7)
print(5 & 4)
print(10 | 7)
print(100 | 7)
print(2 | 3)
print('\n')

print(~3)
print(~(10 & 7))
print(2 ^ 3)
print(10 >> 2)
print(10 << 2)

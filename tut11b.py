# code - 1
# date = 25-4-2022

#* add multiple elements to in tuple

x = tuple(i for i in range(1, 10))
print(x)
print('\n')

x = tuple(i for i in range(2, 10, 2))
print(x)

x = tuple(i for i in range(3, 10, 2))
print(x)
print('\n')

t1 = (32, 34, 35, 36, 37)
t2 = (77, 38, 39, 40, 41)
t3 = t1
t4 = (32, 34, 35, 36, 37)
print(id(t1))
print(id(t2))
print(id(t3))
print(id(t4))

print(t1 == t2)
print(t1 != t3)
print(t1 is t2)
print(t1 is not t4)
print(35 in t4)
print('x' not in t1)
print('\n')

t1 = t1 + t2
print(id(t1))
t1 = t1 *2
print(id(t1))
print('\n')

q1 = (32, 34, 35, 36, 37)
q2 = (326, 314, 325, 336, 373)
q1 = list(q1)
print(q1)
print(id(q1))

q1.append(56)
q1 = tuple(q1)
print(q1)


q2 = (10, 34, 98, 11, 34, 10, 66, 71)
print(q2.count(10))
print(len(q2))
print(q2.index(10))
print(q2.index(10, 2, 5))


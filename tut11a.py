# code - 1
# date = 25-4-2022


#! Tuple 
t = (23, 34, 35, 36, 37, 38, 39)
print(t)

t1 = (23, 34, 35, [43, 67], 'fdg', True)
print(t1)

t2 = ()
t2 = tuple()
print(t2)

t0 = (56)
t = (56,)
print(type(t0))
print(type(t))

t = tuple('Pune')
print(t)
print('\n')

t1 = (23, 34, 35, [43, 67], 'fdg', True)
print(t1[5])
print(t1[3][1])
print(t1[-1])
print('\n')

print(t1[:])
print(t1[:3])
print(t1[::-1])
print('\n')

#* unpaking data
a, b, c = (32, 'fgfg', 23)
t1 = (23, 34, 35, [43, 67], 'fdg', True)
for i in t1:
    print(i)


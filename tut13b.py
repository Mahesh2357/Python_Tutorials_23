# code - 1
# date = 27-4-2022

d = {1:'rrw', 2:34, 3:'sdssd', 4:'MMM'}
for i in d:
    print(i, d[i])
print('\n')

print(d.items())
print('\n')

for i in d.items():
    print(i)
print('\n')
     
for i, j in d.items():
    print(i, j)
print('\n')
     
d = {1:'rrw', 2:34, 'a':'sdssd', 4:'MMM'}
del d['a']
print(d)

d.pop(2)
print(d)
print('\n')

#! del d['u'] => Error

#* popitem() => remove last item
d.popitem()  
print(d)
print('\n')

#! Error => if dict is empty,then popitem gives error
d.clear()
print('Dict is empty.........')
print(d)
print('\n')

d2 = {1:'rrw', 2:34, 'a':'sdssd', 4:'MMM', 'b':' sdssd', 4:'hMMM'}
print(d2[4])
print(id(d2))

print(id(d2[4]))
print(id(d2['a']))
print('\n')

d2['a'] = 'KKKK'
print(d2)
print('\n')

d1 = {11:'3443'}
d3 = {12:'pune'}
d1.update(d3)
print(d1)
print('\n')

d4 = {**d1, **d3}
print(d4)
print('\n')

print(d2)
print(len(d2))
print(len(d2.keys()))
print(len(d2.values()))










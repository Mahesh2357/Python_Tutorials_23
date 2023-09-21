# code - 1
# date = 27-4-2022

#* Dict => case sensitive 
d1 = {}
d2 = dict()
print(d1)
print(d2)
d1['hi'] = 'Welcome'
print(d1)

d = {1:'Hello', 2:'mahesh', 3:'rrr'}
print(d[1])
print(d[2])

print(d.get(1))
print(d.get(4))
print('\n')
#! to get all the keys from of the dictionary use : keys() function
#* to get all the values from of the dictionary use : values() function

print(d.keys())
print(d.values())

print(list(d.keys()))
print(list(d.values()))
print('\n')

print(tuple(d.values()))
print('\n')

#? to print the data in the dictionary using => sorted() function
d = {1:'Hello', 2:'mahesh', 3:'rrr'}
print(sorted(d.keys()))
print(sorted(d.values()))
print('\n')

d1 = {1:'Hello', 2:'mahesh', 3:'rrr'}
d2 = {1:'apple', 2:'kfkf', 3:'4545'}
d3 = d1
d4 = {1:'apple', 2:'kfkf', 3:'4545'}
print(id(d1))
print(id(d2))
print(id(d3))
print(id(d4))
print('\n')

print(d1 == d2)
print(d2 == d3)
print(d3 != d4)
print(d4 == d2)
print('\n')

print(d1 is not d3)
print(d3 is d4)
print(1 in d1)

#! it ckeak only keys not values()
print('rrr' in d1) 
print(3 not in d1)
print('\n')

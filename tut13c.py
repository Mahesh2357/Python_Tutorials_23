# code - 1
# date = 27-4-2022

d = {1:'rrw', 2:34, 'a':'sdssd', 4:'MMM', 'b':' sdssd', 4:'hMMM'}

#! The Zip() function => 
l1 = [1, 2, 3, 4 ,5]
l2 = ['how', 'are', 'you', '. fine', '....']

x = zip(l1, l2)
print(x)
print(dict(x))
print('\n')

l1 = (1, 2, 3, 4 ,5)
l2 = ('how', 'are', 'you', '. fine', '....')
x = zip(l1, l2)
print(x)
print(tuple(x))
print('\n')

s1 = [1, 2, 3, 4, 5]
s2 = ['how', 'are', 'you', '. fine', '....']
t = zip(s1, s2)
print(set(t))

e1 = {1:'rrw',  7:'sdssd', 4:'hMMM'}
e2 = { 4:'MMM',2:34, 9:' sdssd' }
l1 = list(e1.keys())
l2 = list(e2.values())
x = zip(l1, l2)
d = dict(x)
print(d)
print('\n')

e1 = {1:'rrw',  7:'sdssd', 4:'hMMM'}
e2 = { 4:'MMM',2:34, 9:' sdssd' }
l1 = list(e1.keys()) + list(e2.keys())
l2 = list(e2.values()) + list(e1.values())
x = zip(l1, l2)
d = dict(x)
print(d)
print('\n')

print('Different keys same values.....')
l = ['pune', 'Munbai', 'sdds']
d = dict.fromkeys(l, 10)
print(d)
print('\n')

#* Creating dict by using item() method
l = [('cat', 'meow'), ('dog', 'bark'), ('bird', 'chirp')]
x = dict(l)
print(x)

dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}

d = {**dict1 , **dict2 , **dict3}
print(d)

d = dict()
for i in range(1, 11):
    dict1[i] = i*i
print(d)
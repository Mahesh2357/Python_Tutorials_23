# code - 1
# date = 22-4-2022

from audioop import reverse
from os import remove


l = [57, 67, 90, 20, 100, 33, 23]
print('list : ' ,l)
l1 = []
l2 = []

for i in l:
    if i > 50:
        l1.append(i)
    else:
        l2.append(i)
    
print('list-1 : ' , l1)
print('list-2 : ' , l2)
print('\n')

#* to print the index of the element in the list.index()

fruits = ['Apple', 'Orange', 'Mango', 'Orange']
print(fruits.index('Apple'))
print(fruits.index('Mango'))
print(fruits.index('Orange'))

print(fruits.index('Mango', 1))
print('\n')

#! reverse => it is used to reverse the list

f = fruits.reverse()
print(fruits)

# count => to number of elements
print(fruits.count('Apple'))
print(fruits.count('Mango'))
print(fruits.count('M'))
print('\n')

#* sort => method to sort the list
fruits.sort()
print(fruits)

k = [34, 56, 60, 70, 546, 33, 546, 234, 76, 5 ,80, 90, 100 ]
k.sort()
print(k)
print('\n')

#! remove() => remove all items from the list
fruits.remove('Mango')
print(fruits)


# pop() => last item will be remove
fruits.pop()
print(fruits)

fruits = ['Orange', 'Banana', 'Apple', 'Mango']
fruits.pop(2)
print(fruits)

# del statment can also be remove slice from the list
l2 = ['Orange', 34, 436, 43.05, 'cc']
del l2[2]
print(l2)

del l2[2:5]
print(l2)

del l2[:]
print(l2)
print('\n')

l2 = ['Orange', 34, 436, 43.05, 'cc']
l2.clear
print(l2)
print('\n')

l5 = [['a', 2], ['b', 3], ['c', 4], ['d', 5]]
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# [2, 3, 4, 5, 6, 7, 8, 9, 10]
l10 = []
l11 = []

for i, j in l5:
    print(i, j)
    l10.append(i)   
    l11.append(j)
print(l10)
print(l11)
print('\n')


line = 'Welcome to python session'
w = line.split()
print(w)

x = [[w1.upper(), w1.lower(), len(w1)]for w1 in w]
print(x)
print('\n')

i1 =['WeR', 'HrL', 'HrD', 'QeG', 'VxD']
# i.sort()
print(sorted([i.lower() for i in i1]))
print(sorted([i.lower() for i in i1], reverse=True))
print(sorted([i.lower() for i in i1], reverse=False))
# print(i)


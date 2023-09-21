l5 = [10, 20, 30, 40, 50]
# l.append(10)
l5.append(100)
print(l5)
l5.append([False, 4.5])
print(l5)
l5.append((False, 4.5))
print(l5)
print('\n')


l = ['cat', 'dog']
l.insert(1,'rat')
print(l)
l.insert(5, 'dvb')


l1 = [23, 45, True]
l2 = [10, 20, 30, 40, 50, 'dsgf']
l3 = l1 + l2
print(l3)
print(l1 * 3)
print('\n')


l7 =['sdgf', 'dsgf', 'sdfgsfv']
l_copy = l1.copy()
print(l_copy)

print(id(l_copy))
print(id(l1.copy))
print('\n')
# extend() => extend() list by adding all items of a list.

l11 = [23, 45, True]
l21 = [10, 20, 30, 40, 50, 'dsgf']
l11.extend(l21)
print(l11)
print('\n')

# ! why?  => python is interpreted language. it exeucute line by line.
# print(l11.extend(l21)) 

# insert the data in the list

l11 = [23, 45, True]
l11[1] = 'Elephant'
print(l11)

l11[1:5] = 'fox'
print(l11)

l11[3:6] = 100
print(l11)

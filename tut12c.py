# code - 1
# date = 26-4-2022

#* cerating new set by adding list data

l = [43, 2, 45, 616, 70, 80, 80, 901, 'hgghhhg']
s = set()

for i in l:
    s.add(i)
print(s)

#? issubset() => method returns True if all items in the list are existing in specified set , otherwise it returns False

a = {23, 65, 67, 102, 'true', False,55}
b = {67, 102, 'true'}

print(a.issubset(b))
print(b.issubset(a))
print('\n')

#* issuperset =>
print(a.issuperset(b))
print(b.issuperset(a))
print('\n')
#! set difference 
b1 = {'Mango', 'Orange', 'Red', 'Green', 'Yellow'}
b2 = {'Mango', 'Red', 'Green'}
print(b1 - b2)
print(b2 - b1)
print('\n')

# Union of set
print(b1 | b2)
print(b2 | b1)

#! instertion of set
print(b1 & b2)

#* non common elements
print(b1 ^ b2)
print('\n')

#! Q. write a Python program to find common items from two lists.

l1 = [1, 2, 3, 4, 5]
l2 = [1, 22, 33, 4, 35]
s1 = set()
s2 = set()

for i in l1:
    s1.add(i)
for i in l2:
    s2.add(i)
print(list(s1 & s2))
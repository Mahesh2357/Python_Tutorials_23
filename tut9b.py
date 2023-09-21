# code - 1
# date = 21-4-2022

from attr import mutable


l = [10, 20, 30, 40, 50]
l1 = [40, 50, 60, 70, 80]
l2 = [10, 20, 30, 40, 50]


print(l1 is l)
print(l is not l1)
print(l2 is not l1)

print(10 in l)
print(100 in l1)
print('s' not in l1)
print('\n')

# Unpacking the list data
a, b, c, d = [12, True, 34.5, [23, '76d']]
print(a)
print(b)
print(c)
print(d)
print(d[0])
print(d[1])
print('\n')


# iterating through a range using list comprehension
a = [i for i in range(1, 10+1)]
# b = [i for i in range(2, 10)]
print(a)

b = [i*2 for i in range(1, 10+1)]
print(b)

print(a + b)
print('\n')


l = [10, 20, 30, 40, 50]
sum = 0
print('The sum of elements : ')
for i in l:
    sum += i
    print(sum)

# list data is mutable is allows modification
# list.append() will add new items (x) to the end of the list

l5 = [10, 20, 30, 40, 50]
# l.append(10)
print(l.append(100))

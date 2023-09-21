# code - 1
# date = 25-4-2022

t = (10, 34, 98, 11, 34, 10, 66, 71)
print(min(t))
print(max(t))

t1 = ('Pune', 'mumbai', 'nagpur')
print(min(t1))
print(max(t1))
print('\n')

# sort() - present in only list
# sorted() - present in list & tuple
print(sorted(t))
print(sorted(t, reverse=True))
print('\n')

l = list(t)
print(l)
l.sort()
print(tuple(l))

#! Q. assigement.
# b = (4, 3, 2, 2, -1, 18)
# for i in b:
#     b = (i*2)
#     print(b)
    

# b = (4, 3, 2, 2, -1, 18)
# n = 1
# for i in b:
#     n *= i
# print(n)

# #* Q2
# b1 = (2, 4, 8, 3, 2, 9)
# n1 = 1
# for i in b1:
#     n1 *= i
# print(n1)

def multiply(n):
    product = 1
    for i in n:
        product *= i
    return product
t = (4, 3, 2, 2, -1, 18)
print('Product of t : ', multiply(t))
b1 = (2, 4, 8, 3, 2, 9)
print('Product of t : ', multiply(b1))


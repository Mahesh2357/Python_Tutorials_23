# code - 1
# date = 28-4-2022

#! map() function

print(list(map(lambda x:x*2, range(10))))
print(list(map(lambda x:x*3, range(10))))

w = [34, 1, 2, 3, 4, 5, 6, 7 ,56 ,45, 23, 26, 27 , 28]
def convert_Double(w):
    return w + w
double_number = map(convert_Double, w)
print(double_number)
print(list(double_number))

print('The double of given list : ')
print(list(map(lambda x:x+x, w)))
print(list(filter(lambda x:x+x, w)))

#! Add two lists using map and lambda
n1 = [1, 2, 3]
n2 = [4, 5, 6]

res = map(lambda x, y: x + y, n1, n2)
print(list(res))

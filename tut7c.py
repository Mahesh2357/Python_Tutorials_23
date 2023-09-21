
def add():
    a, b = 54, 67
    c = a + b
x = add()
print(x)

def f1(a):
    if a%2 == 0:
        return True
x = f1(6)
print(x)
print('\n')

# pass - is empty statement in python
if 5> 3:
    pass
    print('RFEF')
    for i in range(10):
        pass
    print('Hello, world!')

def f1():
    pass
f1()

#* numbers
#  int/float/complex = type
a = 4
b = 5.6
c = 6j
print(type(a))
print(type(b))
print(type(c))

#* Booleans
#* Logical operator & comparison operator return Booleans values.

#* string => inmuttable
s = 'Welcome to python session'
print(s[3])
print(s[4:10])
print(s[4:16])
print(s[:15])
print(s[5:])
print(s[:])
print(s[::3])
print(s[::-1])
print(s[-17:-2])
print(s[-17::-2])
print(s[-10])

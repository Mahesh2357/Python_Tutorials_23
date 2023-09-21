#! code - 1
#? date = 18-4-2022

# def f1():
#     print('Hello ')
# f1()
#
# num = int(input('Enter a number : '))
# def square(n):
#     print('The square of given number : ', end=' ')
#     print(n * n)
# square(num)
#
# #* using return
# print('**---**---**---**---**---**---**---**')
# def square(n):
#     print('The square of number using return: ', end=' ')
#     return n * n
# s = square(num)
# print(s)

# print(type(square(num)))
a , b = 2, 6
def f2():
    a , b = 34, 56
    print('-----------')
    print('local values.')
    print(a + b)
    print('global values.')
    print(globals()['a'] + globals()['b'])
f2()
print(f2())
print('\n')

def bestwise(name):
    print('Happy Birthday: ' + name)

def main():
    bestwise('mmzf')
    bestwise('mmzf4577')


main()
print('\n')

#* code -5
def outer():
    print('outer function')

    def inner():
        print('inner function')

    inner()


outer()
print('\n')

name1 = 'Mahesh'
def outer():
    print('outer function')

    def inner():
        name2 = 'Mahesh32445'
        print('inner function')
        print(name2)
        print(name1)
    inner()
    print(name1)
outer()
print('\n')


name1 = 'Mahesh'
def outer():
    print('outer function')
    name3 = 'gwsdv23'
    def inner():
        name2 = 'Mahesh32445'
        print('inner function')
        print(name2)
        print(name1)
    inner()
    print(name3)
    print(name1)
outer()
print('\n')

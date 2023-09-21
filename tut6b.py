#! code - 1
#? date = 18-4-2022

# * Non local variables
name1 = 'Mahesh'
def outer():
    print('outer function')
    name3 = 'gwsdv23'
    def inner():
        # nonlocal name1
        name1 = 'Mahesh32445'
        print('inner function')
        # print(name2)
        print(name1)
    inner()
    print(name3)
    print(name1)
    return name1
outer()
print('\n')


name1 = 'Mahesh'
def outer():
    name3 = 'gwsdv23'
    def inner():
        # name2 = 'hdkk'
        name1 = 'Mahesh32445'
        return name1
    n = inner()
    inner()
    print(name1)
    print(n)
outer()
print('\n')


#* use nonlocal
def outer():
    name10 = 'Deepa'
    def inner():
        name20 = 'Uma'
        nonlocal name10
        name10 = 'kkkk'
        print(name10)
        print(name20)

    inner()
    print(name10)
outer()
print('\n')

#* use global
def outer():
    name10 = 'Deepa'
    def inner():
        name20 = 'Uma'
        global name10
        name10 = 'kkkk'
        print(name10)
        print(name20)

    inner()
    print(name10)
outer()
print(name10)
print('\n')


def outer():
    o1 = int(input('Enter the name1 : '))
    o2 = int(input('Enter the name1 : '))
    def inner(o1, o2):
        return o1 + o2

    q = inner(o1, o2)
    print('the sum in outer : ',q)
    inner(o1, o2)
outer()
print('\n')

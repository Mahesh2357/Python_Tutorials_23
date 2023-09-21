#! code - 1
#? date = 18-4-2022

#* defult argument - when we call this function if we are not passing argument the default value is assigned.


# def emp(eid = 44, ename = 'DDDD'):
#     print('Email ID: ' , eid, 'Emp name: ' ,ename)
# emp()
# emp(33, 'RRR')
# emp('WWWE')
# print('\n')

# Required argument - are the medetory argument of function.
# these argument value must be passed in correct number and order during function call.


def add(x, y):
    print('value of add: ')
    print(x + y)
add(44, 66)
print('\n')

# keyword argument - keyword are montioned during function call along with their corresponding value.

def emp(eid, ename):
    print(eid,' - ' ,ename)


emp(eid = '43', ename= 'RR')
emp(ename= 'eee', eid = '56')
print('\n')

# Varible no. argument - if we do know the exact no. of argument that will passed to a function.\

def f1(*Varible_arg): #* => no. of arguments passed
    # print(Varible_arg)
    for i in Varible_arg:
        print(i, end=' ')
f1(23, 45, 54, 4, 'MM')
f1('Hello', 'Welcome')
print(type(f1))
print('\n')

#! Q. Why it should convert into tuples ?
#* => tuples are inmuttable ,

# none - is special constant in Python which is represented absence of value or null.
# void - do not return anything

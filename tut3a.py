#* code- 1
#? date = 12-4-2022

eid, ename, esal = 12, 'ddd', 6000
print('Emp ID : ', eid, '\nEmp name : ', ename, '\nEmp salary : ', esal)
print('\n')

#*code -2

print('Emp ID : %d \nEmp name : %s \nEmp salary : %f' %(eid, ename,esal))
print('Emp ID : %d \nEmp name : %s \nEmp salary : %0.4f' %(eid, ename,esal))
print('\n')

#*code -3
#! .format
print('Emp ID : {} \nEmp name : {} \nEmp salary : {}' .format(eid, ename,esal))
print('\n')

#*code -4
#! Data type => number, set, list, tuple, string, dictionary, Boolean

b = True
print(type(b))
print(5>4)
print(4 != 6)
print('\n')

l = [23, 45, 67, 'dfff', '4.3', True]
print(l)
print(type(l))

#? Creating Empty List
l1 = list()
print(l1)

l2 = []
print(l2)
print('\n')

#! tuple =>
t = (23,  45, 44, 'DFFD', [45, 'dfff', '4.5'])
print(t)
print(type(t))
t1 = tuple()

t2 = ()
print(t1)
print('\n')

#! Set => group of heterogeneous object

s = {34, 67, 'fgfg', True, 324}
print(s)

s1 = set()
print(s1)
print('\n')

#! Dictionary => data stored in format of keys and values
#! mutable

d = {'a':34, 32:56, 67:45, 'b':673}
print(d)

d1 = dict()
print(d1)

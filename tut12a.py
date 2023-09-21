# code - 1
# date = 26-4-2022

#* set - heterogeneous data type.
from attr import mutable
from pyrsistent import discard


s = {34, '43', True, 'gggg', (34, 54) }
print(s)

s1 = {}
print(type(s1))

s2 = set()
print(type(s2))
print('\n')

#! set - is mutable allow modifications
s = {34, '43', True, 'gggg', (34, 54) }
s.add(666)
s.add('fff')
print(s)
print('\n')

s.update([45, 67, 12], {'wewe', 656})
print(s)

s_copy = s.copy()
print(s_copy)

print(id(s))
print(id(s_copy))
print('\n')

#* concatenate, replication are not allowed in set
#! print(s + s_copy)
#! print(s * 2)

#? discard() & remove()
s = {34, '43',66, 101, True, 'gggg', (34, 54) }
s.discard(34)
s.discard((34, 54))
print(s)

#! s.remove('ttt') => error
s.discard('ttt')
s.remove(101)
print(s)


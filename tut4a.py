#* code- 1
#? date = 13-4-2022

#! Number system

#* Binary form
print(0b1111)
#? => 2(1**0) + 2(1**1) + 2(1**2) + 2(1**3) + 2(1**4)
print(0B1111)
print(0B1011)
print('\n')

#* octal form
print(0o7)
#? => 7(8**o)
print(0o567)
#? => 7(8**o) + 6(8**1) + 6(8**2)
print('\n')

#* Dicimal form
print(10)
print(9)
print('\n')

#* Hexadecimal form
# => base - 16
print(0xa)
print(0Xa)
print(0Xf)
#? => 15(16**0)
print(0Xfa)
#? => 15(16**0) + 12(16**0)
print(0Xfc)
print('\n')


#* code- 1
#! Builtin function

print(bin(10))
print(bin(4098))
print('\n')

print(oct(7))
print(oct(234))
print('\n')

print(hex(12))
print(hex(456798))
print('\n')

#* ascii values
print(ord('a'))
print(ord('V'))
print('\n')

#* Basic data type conversions process
print(int(234.898))
print(int(True))
print(bool(0))
print(bool(10))
print(bool(-10))  # =>
print('\n')

print(str(0))
print(type(str(10)))

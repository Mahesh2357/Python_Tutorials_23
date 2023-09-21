# code - 1
# date = 20-4-2022

s2 = '  Welcome TO DDD'

# splitlines - split s into list of strings on per line
print(s2.split())
print(s2.splitlines())
print('\n')


s1 = 'dslfknlsnlnslvDFDDFFDn lsnvlnlfDFDFDnlsf MAHESH ladDSFVfnsljdvnsln'
print(s1.splitlines())
print(s1.lower())
print(s1.upper())
print(s1.title())
print(s1.capitalize())
print('*'.join(s1))
print(s1.replace('lsnvlnlfnlsf', 'MAHESH'))
print('\n')

print(s1.startswith('LL'))
print(s1.startswith('ds'))
print(s1.startswith('ds', 3 ,10))
print(s1.endswith('ln'))
print(s1.swapcase())
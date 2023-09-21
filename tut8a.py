# code - 1
# date = 20-4-2022

#* The len() function return the no. of items.
print(len('Welcome to the Google'))

# == , != operator will check the data comparasion
name1 = 'Google'
name2 = 'MAhesh'
name3 = 'Google'
print(name1 == name2)
print(name2 != name3)
print(name2 == name1)
print('\n')
#? is and is not operator check memory address

print(name1 is name3)
print(name1 is name2)
print(id(name1))
print(id(name2))
print(id(name3))
print('\n')

print(name3 is not name2)
print(name3 in name2)
print(name3 not in name2)
print('\n')

print('Y' in name1)
print('g' in name1)

print('Z' in name2)
print('\n')

# Count - to find data occurrences
s = 'good evening'
print(s.count('o'))

# Concatenation & Replecation
n1 = 'Welcome '
n2 = ' '
n3 = 'Python session '
print(n1 + n2 + n3)
# print(n1 + 10)
print(n1 + n2)
print(n3 * 2)  # Replecation
print(n1 * 6)
print('\n')

# Comparasion operator
m1 = 'Pune'
m2 = 'pune'
print(m1 == m2)
print(m1 > m2)
print(m1 < m2)
print(m1 <= m2)
print(m1 >= m2)
print(m1 != m2)
print('\n')

print('Hello' >= 'hello')

s1 = 'Hello, world'
print(s1.find('l'))
print(s1.find('z'))
print(s1.rfind('o'))
print(s1.rfind('z'))
print('\n')

print(s1.index('l'))
print(s1.rindex('l'))
# print(s1.index('x'))
print('\n')

# strip - copy without leading or trailing spaces
s2 = '  Welcome TO DDD'
print(s2.strip())

s3 = '@@@WELCOME###'
# print(s3.strip())
print(s3.lstrip('@').rstrip('#'))
print(s3.lstrip('@'))
print('\n')

print(s2.split())
print(s2.split('l'))
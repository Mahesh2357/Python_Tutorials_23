# thu 10-5-22

#! File Handling in Python
f = open('samplpppe.txt', 'w')
f.write('WELCOME TO CODE')
f.close()

f = open('sample.txt')
print(f.read())

print(f.tell())
print(f.read())
print(f.seek(5))
f.close()

f = open('sample.txt', 'w')
f.write('Bitcoin doesn’t need backing, be\ncause it is a digital commo\ndity that is valuable itself, and valuable in large part because it carries no physical\n burdens or constr\naints. It is this lack of physical back\ning which enables it to move anywh\nere, instantly, at near-zero cost.')

f.close()

f = open('sample.txt')
print(f.readline())
print(f.readlines())
print('\n')

f.seek(45)
print(f.readline())
print('\n')

f.seek(0)
print(f.readlines())
print('\n')


#!====================================

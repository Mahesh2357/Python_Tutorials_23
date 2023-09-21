# Wed 11-5-22

# f = open('demo.txt', 'r')
f = open('demo.txt', 'a')
# print(f.read())
print(f.write('HELLO, Im am awesome \n'))
f.close()

f = open('demo.txt')
print(f.read())
print(f.name)
print(f.mode)

print(f.closed)
f.close()
print(f.closed)

print('\n')

#! with statements => when we declare the file by using the with statement

with open('demo.txt') as fh:
    print(fh.read())
    print(fh.read())
print(fh.closed)
print('\n')
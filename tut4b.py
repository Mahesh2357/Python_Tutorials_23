#* if statement
#? => Desision making is required when we want to execute a code
#? only if a certain condition is true.

result = 37
if result >= 40:
    print('Pass')
else:
    print('Fail')

#! for Grade
result = 87

if result >= 70:
    print('A+')
elif result >= 60:
    print('A')
elif result >= 50:
    print('B+')
elif result >= 40:
    print('B')
else:
    print('Fail')

#* One line code
x = 'Pass' if result >= 70 else 'Fail'
print(x)
print('\n')

#* COde for Positive and Negative numbers
n = 5
c = 'Positive' if n > 0 else 'Negative' if n < 0 else 'Zero'
print(c)

#* Loop
# in python dowhile loop not exists
#! While loop

'''while text expression:
    block of code'''

#* Q. Program to calculate the gcd of the two numbers.
a = 4
b = 8
while(a != b):
    if(a == b):
        a -= b
    else:
        b -= a
print('GCD of the two numbers : ', a)

#* Q. Write the Program to print the number of digit of a
#* given number using the while loop.

n = 4523434
digit = 0
while n != 0:
    n = n // 10
    digit += 1
print('digit : ', digit)
print('\n')


#* FOr Loop

#! syntax:
#? For <temp-varible> in <sequence-date>:
#?    body for statement(s)

#* Range Function
#* range(10) : 1 2 3 4 5 6 7 8 9
#* range(0, 10, 3) : 0 3 6 9

for i in range(10):
    print(i, end=' ')
    print(i, end='-')
print('\n')

for e in range(1, 10):
    print(e, end=' ')
print('\n')

for e in range(1, 10+1, 3):
    print(e, end=' ')
print('\n')

#* List
l = [34 ,56 ,67 ,'Hello']
for i in l:
    print(i, end=' ')
print('\n')

#* Tuples
t = (213, 567, 56, 'erwe', 3)
for i in t:
    print(i, end=' ')
print('\n')

#* Dict
d = {'g':'43', 'b':'34', 'fd':'asqw'}
for i in d:
    print(i , d[i])
print('\n')

#* Q. Write a Program to verify if a given number is Prime or Non-prime.

f = 1033455476
flag = True
for i in range(2, f):
    if f%i == 0:
        flag = False
print('Prime' if flag == True else 'Not prime')

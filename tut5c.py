#* code- 1
#? date = 14-4-2022

#* Using while loop
# i = 1
# while(i<=20):
#     if i%2 == 0:
#         print(i, end=' ')
#     if i == 6:
#         # break
#         # i/0
#         import os
#         os._exit(0)
#     i += 1
# else:
#     print('\nEven numbers.')
# print('\n')

#* Q, To print the prime number between 5 to 50

a = 5
b = 50
print('Prime numbers :')
for i in range(a, b+1):
    if i>1:
        for n in range(2, i):
            if i%n == 0:
                break
        else:
            print(i, end=' ')
print('\n')


a = 5
b = 50
for i in range(a, b+1):
    if i>1:
        for n in range(2, i):
            if n%i == 0:
                break
        else:
            print(n, end=' ')
print('\n')

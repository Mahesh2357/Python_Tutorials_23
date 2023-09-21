#* code- 1
#? date = 14-4-2022

#* in 3 cases the else block is not executed.
#* 1. if excption is occuring.
# for i in range(10):
#     if i == 5:
#       i/0
#     print(i, end=' ')
# else:
#     print('After complete iteration of for loop execute the else block')
# print('\n')

#* 2.
# for i in range(10):
#     if i == 5:
#       # i/0
#       break
#     print(i, end=' ')
# else:
#     print('After complete iteration of for loop execute the else block')
# print('\n')


#* 3. if we are shutting down virtual machine, than
# for i in range(10):
#
#     if i == 5:
#       import os
#       os._exit(0)
#     print(i, end=' ')
# else:
#     print('After complete iteration of for loop execute the else block')
# print('\n')

#* while loop
#! Q. why python provides else block in loop ? => excption handling, break statement,

#* Using For loop
for i in range(30):
   if i%2 == 0:
     print(i, end=' ')
else:
    print('\nEven numbers.')
print('\n')

#* Using while loop
i = 1
while(i<=20):
    if i%2 == 0:
        print(i, end=' ')
    i += 1
else:
    print('\nEven numbers.')
print('\n')

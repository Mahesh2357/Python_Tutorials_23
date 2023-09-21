#* code- 1
#? date = 14-4-2022

#* Break => 
#* Break statement is used to stop the code execution.
#* Break statement terminates the loop containing it.
#* if Break statement is inside a nasted loop (loop inside another loop)
#* Break will be terminated the intermost loop.

for i in range(10):
    if i == 5:
        break
    print(i, end=' ')
print('\n')


name = 'Welcome'
for i in name:
    if i == 'o' or i == 'l':
        break
    print(i, end=' ')
print('\n')


name = 'Welcome'
for i in name:
    if i == 'o' and i == 'l':
        break
    print(i, end=' ')
print('\n')

#* continue =>
#* Continue used to skip the perticular iteration.
#* loop do not terminate but continue on with the next iteration.

for i in range(10):
    if i ==5:
        continue
    print(i, end=' ')
print('\n')


for i in 'Welcome':
    if i == 'o' or i == 'l':
        continue
    print(i, end=' ')
print('\n')

for i in 'Welcome':
    if i == 'o' and i == 'l':
        continue
    print(i, end=' ')
print('\n')


#* else block is always executed if the for loop terminated normally.

for i in range(10):
    i/0
    print(i, end=' ')
else:
    print('After complete iteration of for loop execute the else block')
print('\n')

i = 1
while(i<=20):
   if i%2 == 0:
     print(i, end=' ')
   i += 1
else:
    print('\nEven numbers.')

# code - 1
# date = 22-4-2022

# Q. Write a program to get the latest number from the list.
# Q. Write a program to get the smallest number from the list.


k = [34, 56, 60, 70, 546, 33, 546, 234, 76, 5 ,80, 90, 100]
k.sort()
print('largest no. of list: ', k[-1])
print('smallest no. of list: ', k[0])
print('\n')

print(max(k))
print(min(k))


#! Q. Write a program to count the number of strings where the string length
#!  is 2 or more than first and last charater are same from a given list of strings.

l9 = ['abc', 'def', 'ada', '1221']

count = 0
for i in l9:
    if (len(i)>1 and (i[0]==i[-1])):
        count += 1
    print(count)
    
print('\n')
print(count)

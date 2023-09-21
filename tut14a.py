# code - 1
# date = 28-4-2022

#! Lambda Function => a small anonymous function (name less function) to perform operations.

# to print square of any number using void functions
def print_square(x):
    print('Square of number : ',x * x)
print_square( 4)
print('\n')

a = lambda x: x * x
print(a(4))

c = lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Zero'
print(c(4))

#! Use of lambda functions
#* lambda functions are used along with built-in functions like filter() and map()

# filter() function
print(list(filter(lambda x: x%2 == 0, range(10))))
print(list(map(lambda x: x%2 == 0, range(10))))

n = 'MAHESH'
print(list(filter(lambda x: x == 'H', n)))
print('\n')

#! to filter even numbers from the list
t = [34, 342, 434, 45, 12, 13, 14 , 67, 45, 90, 345, 78, 88]
def check_EvenNumbers(t):
    if t % 2 == 0:
        return True
    return False
even_numbers = filter(check_EvenNumbers, t)
print(even_numbers)
print('The list of even numbers : ')
print(list(even_numbers))
print('\n')

#! Error
#! print(list(filter(lambda t:True if t % 2 == 0 else False )))
print('The list of even numbers : ')
print(list(filter(lambda t: t % 2 == 0 , t)))

print('The list of odd numbers : ')
print(list(filter(lambda t: t % 2 != 0 , t)))


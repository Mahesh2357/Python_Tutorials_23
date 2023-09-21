# code - 1
# date = 20-4-2022

s = 'Python310'
s1 = 'Python 310'

#* The isalnum() function checks whether the argument passed is an alphanumeric character (alphabet or number) or not. 
print(s.isalnum())
print(s1.isalnum())

s2 ='2354'
#* The isdigit(c) is a function in C which can be used to check if the passed character is a digit or not. 

print(s2.isdigit())

s3 ='dfsd fsfpe'
print(s3.isalpha())
print(s3.islower())
print(s3.isupper())
print(s3.isspace())
print(s3.title())
print(s3.isspace())
print('\n')
# enumerate function - function returns sn enumearte objects.
# it consisting of the index and value of the all the items in the string as pairs

r = 'welcome to python session'
print(enumerate(r))
print(list(enumerate(r)))
print(tuple(enumerate(r)))
print(dict(enumerate(r)))

# to count the 'a' from the string without count.
w = 'Amarawati'
# print(w.find('a'))

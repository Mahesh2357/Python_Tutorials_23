# Mon 2-5-22

#* A class is a user-defined blueprint or prototype from which objects are created.
class User:
    x = 6
    
o1 = User()
print('The value of x : ',o1.x)
print('\n')


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
o1 = Employee('Mahesh', 33)
print('The Name of employee : ',o1.name,'\nThe age of employee : ', o1.age)

#! In Python, the pass keyword is used to execute nothing; it means, when we don't want to execute code, the pass can be used to execute empty.


class Object:
    pass
obj= Object()
print(obj)

class ee:
    a = 23
    b = 42
    c = a + b
o = ee()
print('Sum : ', o.c)

print(o.a)
print(o.b)
print(o.c)


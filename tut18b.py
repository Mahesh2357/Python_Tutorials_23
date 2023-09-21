
#! __str__() => return always string only

class my_class2:
    def __str__(self):
        # print('STR constructor')
        return '67'

c = my_class2()
print(c)

class Employee:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        
    def __str__(self):
        return 'Emp id : %d\n name : %s\n age : %s' % (self.id, self.name, self.age)
e1 = Employee(23, 'MAHESH', 123)
e2 = Employee(23, 'MAHESH', 123)
print(e1)
print(e2)
print('\n')

#* when obj is deleted then del constructor is called

class vechile:
    def __init__(self):
        print("MY vechile")
    def __del__(self):
        print("Obj deleted")    
v= vechile()
c = v
c1 = v
del v
print(c)
print(id(c))
print(id(c1))

#! local varibles vs global variables vs class variables.
a, b = 10, 20
class myclass:
    a, b = 101, 201
    
    def add(self,a ,b):
        print("adding local values :", end='')
        print(self.a + self.b)
        
        print("adding global values :", end='')
        print(globals()['a'] + globals()['b'])
        
        print("adding class values :", end='')
        print(a + b)

c = myclass()
c.add(1, 2)
print('\n')

#! 1. Name obj
#! types of objects : 
#! 1. Nameless obj

class myclass1:
    def display(self):
        print("HELLO")
c = myclass1()        #! name obj
c.display()

myclass1().display()    #! name obj


class myclass2:
    name = 'myclass'
v = myclass2()
print(v.name)

v.name = 'myclass 3223'
print(v.name)

v1 = myclass2()
print(v1.name)
print('\n')

#! ========
class myclass4:
    def f1(self):
        print("HELLO.....MAHESH")
    @staticmethod
    
    def f2():
        print("static method...... ")
    @staticmethod
    
    def f3():
        print('one more static method....')
c= myclass4()
c.f1()   #! acess instance method
c.f2() #! acess static method
c.f3()
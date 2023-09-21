'''
          Encapsulation
Wrapping up of data members and member functions into a single unit called class is called as Encapsulation.
Data should not be used outside the object , so, we use Encapsulation.

'''

class myclass:
 #   _a = 10 # Data is private here
     def _f1(self):
         print("hello")
c = myclass()
# print(c.a)
c._f1()

'''
             Polymorphism
Implementing same thing in a different way.
Polymorphism refers to the use of a single type entity (method, operator or object)
to represent different types in different scenarios.
 
Polymorphism stands with 2 ways:
1) Overloading
2) Overriding

'''
'''
Overloading Operator: + operator is used extensively in python programs. But it does not have a single usage.
'''
print(4 + 9)
print('hello' + 'welcome')
print(5 * 2)
print("hello" * 2) # replication of data

# Overloading function: There are some functions in python which are corresponding to run with multiple data types.

l = [56, 89, 34, 7.8]
print(len(l))
print(len("Welcome"))
d = {56 : 'vhbfj', 'er' : 'fvgybf', 5 : 8987}
print(len(d))

print("*****************************************")

# Overloading class : Creating class methods as python alllows different classes to have different methods with the same name.

class Cat:
    def __init__(self, name):
        self.name = name
    def info(self):
        print("I am a cat, my name is: ", self.name)
    def makesound(self):
        print("I do meow")

class Dog:
    def __init__(self, name):
        self.name = name
    def info(self):
        print("I am a dog, my name is: ", self.name)
    def makesound(self):
        print("I do bark")

c = Cat('Pussy')
d = Dog("Fluffy")

for i in (c, d):
    i.info()
    i.makesound()


print("************************************************")

'''
Method Overriding: The child classes inherit methods and attributes from the parent class. 
We can redefine certain methods and attributes specifically to fit the child class, this is known as Method Overriding. 

Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class.
'''

from math import pi
class Shape:
    def __init__(self, name):
        self.name = name # initialising at the class level
    def area(self):
        pass
    def __str__(self):
        return self.name
class Square(Shape):
    def __init__(self, length):
        self.length = length
        return super().__init__("Square")
    def area(self):
        return self.length ** 2
    #def __str__(self):
     #   return super().__init__("Square") # calling parent class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        return super().__init__("Circle")
    def area(self):
        return pi * (self.radius ** 2)
    #def __str__(self):
      #  return super().__init__("Circle")
s = Square(4)
print(s)
c = Circle(5)
print(c)
print(s.area())
print(c.area())

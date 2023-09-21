# Mon 9-5-22

#! Hirarchical Inheritance =>
class Parent:
    def __init__(self):
        print('Parent class constructor')
    
class Child1(Parent):
    def __init__(self):
        print('Child1 class constructor')
        super().__init__()

class Child2(Parent):
    def __init__(self):
        print('Child2 class constructor')
        super().__init__()
        
class Child3(Parent):
    def __init__(self):
        print('Child3 class constructor')
        super().__init__()
        
c1 = Child1()
print('\n')
c2 = Child2()
print('\n')
c3 = Child3()
print('\n')

#! Hybrid inheritance
#! ======================================
class University:
    def __init__(self):
        print('List of students and Branches...')

class Branches(University):
    def __init__(self):
        print('Pune branch...')
    
class Course(University):
    def __init__(self):
        print('Course Name ...')

class Student(Course, University):
    def __init__(self):
        University.__init__(self)
        Course.__init__(self)
        print('Student Name ...')

o1 = Student()

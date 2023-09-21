'''
           Hierarchical Inheritance
When more than one derived classes are created form a single base class, this type of inheritance is called as hierarchical inheritance.

'''

class Parent:
    def __init__(self):
        print("Parent class")
class Child1(Parent):
    def __init__(self):
        print("Child 1 class")
        super().__init__()
class Child2(Parent):
    def __init__(self):
        print("Child 2 class")
        super().__init__()
class Child3(Parent):
    def __init__(self):
        print("Child 3 class")
        super().__init__()
c1 = Child1()
c2 = Child2()
c3 = Child3()

print("************************************************")
'''

           Hybrid Inheritance
Hybrid inheritance involves multiple inheritance taking place in a single program.           
'''
class University:
    def __init__(self):
        print("List OF Students and Branches")
class Branches(University):
    def __init__(self):
        print("PUNE Branch")
class Courses(University):
    def __init__(self):
        print("Course Name")
class Student(Courses, University):
    def __init__(self):
        University.__init__(self)   # - Nameless Object
        Courses.__init__(self)
        print("Student Name")
s = Student()


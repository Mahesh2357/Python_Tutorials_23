class A:
    def met(self):
        print('This is method called from a class A')
        
class B:
    def met(self):
        print('This is method called from a class B')

class C:
    def met(self):
        print('This is method called from a class C')

class D(C, B):
    def met(self):
        print('This is method called from a class D')

# a = A()
# b = B()
# c = C()
d = D()
# print(a, b, c, d)
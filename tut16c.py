# def split1(func):
#     def wrapper():
#         data = func('*******')
#         return '*********\n ======'
#         # return '*********\n ======'
#     return wrapper

# def split2(func1):
#     def wrapper1():
#        data1 = func()
#        return '======='
#     return wrapper1
# @split1
# @split2

# def greet():
#     return'Hello, Guys....'
# print(greet())
# print('\n')

class Rect1:
    def __init__(self, c,l,w):
        self.colour = c
        self.length = l
        self.width = w

    def area(self):
        self.area = self.length * self.width
        return self.area
        
    def perimeter(self):
        self.perimeter = 2* self.length + 2* self.width
        return self.perimeter

    def diag(self):
        self.diag = (self.length**2 + self.width**2) **(1/2)
        return self.diag
    
    def Vol(self, h):
        self.height = h
        self.vol = self.length * self.width * self.height
        return self.vol
                
myRect1 = Rect1('RED', 2,1)
myRect2 = Rect1('Green', 1,12)

print(myRect1.colour)
print(myRect2.colour)
print('\n')

print('The length of rect1 : ', myRect1.length)
print('The length of rect2 : ', myRect2.length)
print('\n')

print('The width of rect1 : ', myRect1.width)
print('The width of rect2 : ', myRect2.width)
print('\n')
        
# area=myRect1.area
# area = myRect2.area
print('The area of rect1 : ', myRect1.area(), 'in units')
print('The area of rect2 : ', myRect2.area(), 'in units')
print('\n')

print('The diagonal of rect1 : ', myRect1.diag())
print('The diagonal of rect2 : ', myRect2.diag())
print('\n')

print('The Vol of cuboid : ', myRect1.Vol(2))
print('The Vol of cuboid : ', myRect2.Vol(4))


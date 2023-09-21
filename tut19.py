
# #! === Inheritance === 
# class First_class:
#     def __input1__(self):
#         self.x = int(input("Enter first number : "))
#         self.y = int(input("Enter second number : "))

# class Third_class(First_class):
#     def __add__(self):
#         super().__input1__()
#         self.z = self.x + self.y
#         print("Sum is:", self.z)

# o1 = Third_class()
# o1.__add__()

#! ==============================
class setData:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print('Sum is : ', self.x + self.y)

class addtion(setData):
    def __init__(self):
        super().__init__(2, 5)
        
c= addtion()
# print(c)

        
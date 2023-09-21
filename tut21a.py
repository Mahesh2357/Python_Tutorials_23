# thu 10-5-22

#! Abstraction --->
#* to create a Abstract class => Use module ABC
from abc import ABC, abstractmethod

class Abstractdemo(ABC):
    @abstractmethod
    def display(self):
        pass    #! only decleration not defination
    
    @abstractmethod
    def show(self):
        pass
    
class demo(Abstractdemo):
    def display(self):
        print('Abstract demo')

    def show(self):
        print('Show function')
        print(66 + 3)

o1 = demo()
o1.display()
o1.show()
print('\n')


class Mammal:
    def __init__(self, m_name):
        print(m_name, 'is warm -blooded animal...')

class Animal(Mammal):
    def __init__(self, a_name):
        super().__init__(a_name)
        print(a_name, ' has four legs...')
a = Animal('Sheep')
print('\n')


#! ====== === ====== === ======
class Mammal:
    def __init__(self, m_name):
        print(m_name, 'is warm -blooded animal...')

class Animal(Mammal):
    def __init__(self, a_name):
        super().__init__(a_name)
        print(a_name, ' has four legs...')

ani = input('Enter the Animal name : ')
a = Animal(ani)
print('\n')


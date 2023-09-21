# Fri 29-4-22

def makedecorator(func):
    def wrapper():
        print('I am a decorator function')
        func()
    return wrapper
@makedecorator

def general_func():
    print('HELLO')
general_func()
print('\n')


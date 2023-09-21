
#! File operation module : os

import os
# print(dir(os))
# os.rename('sample.txt', 'sam.txt')

# os.remove('sam.txt')
# os.mkdir('New')

# os.chdir('sample.txt')
# os.chdir('./')

os.chdir('./')
os.chdir('../')   #!(1st-dot) is outside the root directory (2nd-dot) inside the root directory 
print('new path', os.getcwd())



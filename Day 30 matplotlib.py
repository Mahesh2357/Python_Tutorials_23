"matplotlib"
"most of the matplotlib utilities lies under the plotlib"
import matplotlib.pyplot as plt
#import numpy as np
'''x = np.array([3,15])
y = np.array([1,8])
plt.plot(x,y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('LIne graph')
plt.show()'''
line = [1,2,4,5]
height = [45,23,21,2,17]
plt.bar(line, height)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Bar graph')
plt.show()

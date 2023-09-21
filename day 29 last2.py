'''import matplotlib.pyplot as plt
Line=[1,2,3,4,5]
Height=[45,23,21,2,17]

plt.bar(Line,Height)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Bar graph")
plt.show()'''


import matplotlib.pyplot as plt
activity=['eat','sleep','work','play']
slices=[3,7,8,6]

plt.pie(slices, labels=activity,explode=(0,0,0.1,0), autopct='%1.1f%%')  #u can do 0.9 also
plt.title("Pie graph")
plt.legend()
plt.show()
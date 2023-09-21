import matplotlib.pyplot as plt

activity = ['eat','sleep','work','play']
slice=[3,7,8,6]
plt.pie(slice,labels=activity, explode=(0,0,0,0),autopct='%1.1f%%')
"to explode use this term above"
plt.title('Pie chart')
plt.legend()
plt.show()


activity = ['eat','sleep','work','play', 'mm']
slice=[3,7,8,6, 5]
plt.pie(slice,labels=activity, explode=(0,0,0.1,2, 1),autopct='%1.1f%%')
"to explode use this term above"
plt.title('Pie chart')
plt.legend()
plt.show()


activity = ['eat','sleep','work','play', 'mm']
slice=[3,7,8,6, 5]
plt.pie(slice,labels=activity, explode=(0,0,0,0, 0),autopct='%1.1f%%')
"to explode use this term above"
plt.title('Pie chart')
plt.legend()
plt.show()


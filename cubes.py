import matplotlib.pyplot as plt 

# x_values = [1,2,3,4,5]
x_values = range(1,1001)
y_values = [x**3 for x in x_values]
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# ax.plot(x_values,y_values)
ax.scatter(x_values, y_values,c=x_values, cmap=plt.cm.Blues, s= 20)
ax.set_title('Cubes of numbers')
ax.set_xlabel('values')
ax.set_ylabel('cubes of values')
ax.axis([0,1100,0,1100000000])
ax.tick_params(labelsize=14)
ax.ticklabel_format(style='plain')
plt.show()
import matplotlib.pyplot as plt
# input_values = [1,2,3,4,5]
# squares = [1,4,9,16,25]

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# scatter plot with single value
# ax.scatter(2,4, s=2000)

# scatter plot with muliple points
# ax.scatter(input_values,squares, s=200)

# ax.scatter(x_values,y_values,color='red',s=20)
ax.scatter(x_values,y_values,c=x_values, cmap=plt.cm.Blues,s=20)

ax.set_title('Sqaure numbers', fontsize=24)
ax.set_xlabel('value',fontsize=13)
ax.set_ylabel('sqaure of value', fontsize=13)
ax.axis([0,1100,0,1_100_000])
# set size of tick labels
ax.tick_params(labelsize=14)
ax.ticklabel_format(style='plain')
plt.show()
# plt.savefig('sqaures_plot.png',bbox_inches='tight')

from die import Die
import plotly.express as px

die_1 = Die()
die_2 = Die()
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
frequencies = []
max_result = die_1.num_sides+die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequencie = results.count(value)
    frequencies.append(frequencie)

# print(results)
# print(frequencies)

# visualize the results

fig = px.bar(x=poss_results, y=frequencies, title="Results of Rolling two Dice Roll", labels={'x':'Result','y':'Frequency of Result'})
# Further customize the chart 
fig.update_layout(xaxis_dtick=1)
fig.show()

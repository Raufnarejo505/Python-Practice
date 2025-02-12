from die import Die
import plotly.express as px

# create a D6 and D10 
die_1 = Die()
die_2 = Die(10)
results = []
for roll_num in range(50000):
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

fig = px.bar(x=poss_results, y=frequencies, title="Results of Rolling a D6 and D10 Dice 50,000 times", labels={'x':'Result','y':'Frequency of Result'})
# Further customize the chart 
fig.update_layout(xaxis_dtick=1)
fig.write_html('dice_visual_d6d10.html')


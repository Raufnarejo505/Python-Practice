from die import Die
import matplotlib.pyplot as plt

die_1 = Die()
die_2 = Die()

max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2,max_result + 1)

results = []
for value in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
for value in poss_results:
    frequencie = results.count(value)
    frequencies.append(frequencie)


fig, ax = plt.subplots()
ax.scatter(poss_results, frequencies, s=10)

plt.show()
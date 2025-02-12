from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract high temparatures
dates, highs, lows =[],[],[]
for row in reader:
    low = int(row[5])
    lows.append(low)
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(current_date)
    high = int(row[4])
    highs.append(high)
print(highs)

# plot the high temparatures
plt.style.use('seaborn-v0_8-bright')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates,lows, color ='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format plot
ax.set_title("Daily high  and low temparatures, 2021", fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('Temparatures (F) ', fontsize = 16)
ax.tick_params(labelsize=16)

plt.show()
# for index, column_header in enumerate(header_row):
#     print(index, column_header)



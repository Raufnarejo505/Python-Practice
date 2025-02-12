from pathlib import Path
import json
import plotly.express as px

# read data as a string and convert to a python object.
path = Path('eq_data/eq_1_day_ml.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# create a more readable vrsion of the data file
path = Path('eq_data/readable_eq_data.json')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Examine all earthquakes in the dataset
all_eq_dicts = all_eq_data['features']

mags , lons, lats, eq_titles= [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)
    eq_titles.append(eq_title)
mags = [max(0,mag) for mag in mags]
title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon = lons, size=mags, title=title,
                     color = mags,
                     color_continuous_scale = 'Viridis',
                     labels = {'color': ' Magnitude'},
                     projection = 'natural earth',
                     hover_name = eq_titles)
                    

fig.show()


#  we can use many other color scales from many available scales using the :
#  px.colors.named_colorscales()

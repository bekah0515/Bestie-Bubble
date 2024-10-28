#!/usr/bin/env python3

import pandas
import plotly.express as px
import random

def euclid_grapher(distances, user_name):
    #distances needs to be pandas dataframe
    #user_name is name of person taking personality quiz as string
    return


names = ['Abigail', 'Beth', 'Chris', 'Dwayne', 'Ella', 'Francine', 'Greg', 'Hugh', 'Indigo', 'Jack']

euclid_distances = {}
for name in names:
    euclid_distances[name] = random.random()

euclid_distances['Simon'] = 0
sorted_distances = sorted(euclid_distances, key=euclid_distances.get)

sorted_dict = {}
for distance in sorted_distances:
    sorted_dict[distance] = euclid_distances[distance]

colors = ['black'] * len(sorted_dict)
colors[0] = 'magenta'
colors[1] = '#FFD700'
colors[2] = '#C0C0C0'
colors[3] = '#CD7F32'
colors[len(sorted_dict)-1] = "#8FC554"

markers = ['circle'] * len(sorted_dict)
markers[0] = 'star'

sizes = [5] * len(sorted_dict)
sizes[0] = 20

names = [''] * len(sorted_dict)
names[0] = sorted_distances[0] + " 🦄"
names[1] = sorted_distances[1] + " 🥇"
names[2] = sorted_distances[2] + " 🥈"
names[3] = sorted_distances[3] + " 🥉"
names[len(sorted_dict) -1] = sorted_distances[len(sorted_dict)-1] + " 🐸"

column_label = ['Distance']
distances = pandas.DataFrame.from_dict(sorted_dict, orient='index', columns=column_label)
distances['color'] = colors
distances['marker'] = markers
distances['y-axis'] = 0
distances['size'] = sizes
distances['name'] = names



fig = px.scatter(distances, x='Distance', y='y-axis', color='color', 
                 color_discrete_map='identity', symbol='marker', 
                 symbol_map='identity', size='size', title='Distances from Bestie Matches')
fig.update_traces(offsetgroup=0)
fig.update_yaxes(visible=False)
for distance in sorted_distances:
    if names[sorted_distances.index(distance)] != "":
        fig.add_annotation(x=sorted_dict[distance],y=0, 
                           text=names[sorted_distances.index(distance)], 
                           showarrow=True, arrowhead=1, textangle=75)
fig.write_image(f"images/{sorted_distances[0]}_bestie_matches.png", scale=2)
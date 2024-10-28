#!/usr/bin/env python3

import pandas, os
import plotly.express as px


similarity_dict = {}
jaccard_similarity = {}
with open('categorical_similarity.txt', 'r') as read_file:
    for line in read_file:
        line = line.rstrip()
        [name, jaccard, gower] = line.split('\t')
        similarity_dict[name] = {}
        similarity_dict[name]['Jaccard'] = float(jaccard)
        similarity_dict[name]['Gower'] = float(gower)
        jaccard_similarity[name] = float(jaccard)

sorted_sims = sorted(jaccard_similarity, key=jaccard_similarity.get, reverse=True)

sorted_dict = {}
for name in sorted_sims:
    sorted_dict[name] = {}
    sorted_dict[name]['Jaccard'] = similarity_dict[name]['Jaccard']
    sorted_dict[name]['Gower'] = similarity_dict[name]['Gower']


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
names[0] = sorted_sims[0] + " 🦄"
names[1] = sorted_sims[1] + " 🥇"
names[2] = sorted_sims[2] + " 🥈"
names[3] = sorted_sims[3] + " 🥉"
names[len(sorted_dict) -1] = sorted_sims[len(sorted_dict)-1] + " 🐸"

text_position = ['top center'] * len(sorted_dict)
text_position[1] = 'bottom center'
text_position[3] = 'bottom center'

column_label = ['Jaccard','Gower']
similarities = pandas.DataFrame.from_dict(sorted_dict, orient='index', columns=column_label)
similarities['color'] = colors
similarities['marker'] = markers
similarities['y-axis'] = 0
similarities['size'] = sizes
similarities['name'] = names
similarities['textposition'] = text_position

if not os.path.exists('images'):
    os.mkdir('images')


fig1 = px.scatter(similarities, x='Gower', y='y-axis', color='color', color_discrete_map='identity', symbol='marker', symbol_map='identity', size='size')
fig1.update_yaxes(visible=False)
fig1.update_layout(xaxis_title='Gower Similarity')
fig1.add_annotation(x=similarity_dict[sorted_sims[0]]['Gower'],y=0, text=names[0], showarrow=True, arrowhead=1, textangle=75)
fig1.add_annotation(x=similarity_dict[sorted_sims[len(sorted_sims)-1]]['Gower'],y=0, text=names[len(sorted_sims)-1], showarrow=True, arrowhead=1, textangle=75)
if similarity_dict[sorted_sims[0]]['Gower'] == similarity_dict[sorted_sims[1]]['Gower']:
    fig1.add_annotation(x=similarity_dict[sorted_sims[1]]['Gower']-.05,y=0, text=names[1], showarrow=True, arrowhead=1, textangle=75)
else:
    fig1.add_annotation(x=similarity_dict[sorted_sims[1]]['Gower'],y=0, text=names[1], showarrow=True, arrowhead=1, textangle=75)
if similarity_dict[sorted_sims[1]]['Gower'] == similarity_dict[sorted_sims[2]]['Gower']:
    fig1.add_annotation(x=similarity_dict[sorted_sims[2]]['Gower']-.05,y=0, text=names[2], showarrow=True, arrowhead=1, textangle=75)
else:
    fig1.add_annotation(x=similarity_dict[sorted_sims[2]]['Gower'],y=0, text=names[2], showarrow=True, arrowhead=1, textangle=75)
if similarity_dict[sorted_sims[2]]['Gower'] == similarity_dict[sorted_sims[3]]['Gower']:
    fig1.add_annotation(x=similarity_dict[sorted_sims[3]]['Gower']-.05,y=0, text=names[3], showarrow=True, arrowhead=1, textangle=75)
else:
    fig1.add_annotation(x=similarity_dict[sorted_sims[3]]['Gower'],y=0, text=names[3], showarrow=True, arrowhead=1, textangle=75)
fig1.write_image(f"images/{sorted_sims[0]}_gower_matches.png", scale=2)


fig2 = px.scatter(similarities, x='Jaccard', y='y-axis', color='color', color_discrete_map='identity', symbol='marker', symbol_map='identity', size='size')
fig2.update_yaxes(visible=False)
fig2.update_layout(xaxis_title='Jaccard Similarity')
fig2.add_annotation(x=similarity_dict[sorted_sims[0]]['Jaccard'],y=0, text=names[0], showarrow=True, arrowhead=1, textangle=75)
fig2.add_annotation(x=similarity_dict[sorted_sims[len(sorted_sims)-1]]['Jaccard'],y=0, text=names[len(sorted_sims)-1], showarrow=True, arrowhead=1, textangle=75)
if similarity_dict[sorted_sims[0]]['Jaccard'] == similarity_dict[sorted_sims[1]]['Jaccard']:
    fig2.add_annotation(x=similarity_dict[sorted_sims[1]]['Jaccard']-.05,y=0, text=names[1], showarrow=True, arrowhead=1, textangle=75)
else:
    fig2.add_annotation(x=similarity_dict[sorted_sims[1]]['Jaccard'],y=0, text=names[1], showarrow=True, arrowhead=1, textangle=75)
if similarity_dict[sorted_sims[1]]['Jaccard'] == similarity_dict[sorted_sims[2]]['Jaccard']:
    fig2.add_annotation(x=similarity_dict[sorted_sims[2]]['Jaccard']-.05,y=0, text=names[2], showarrow=True, arrowhead=1, textangle=75)
else:
    fig2.add_annotation(x=similarity_dict[sorted_sims[2]]['Jaccard'],y=0, text=names[2], showarrow=True, arrowhead=1, textangle=75)
if similarity_dict[sorted_sims[2]]['Jaccard'] == similarity_dict[sorted_sims[3]]['Jaccard']:
    fig2.add_annotation(x=similarity_dict[sorted_sims[3]]['Jaccard']-.05,y=0, text=names[3], showarrow=True, arrowhead=1, textangle=75)
else:
    fig2.add_annotation(x=similarity_dict[sorted_sims[3]]['Jaccard'],y=0, text=names[3], showarrow=True, arrowhead=1, textangle=75)

fig2.write_image(f"images/{sorted_sims[0]}_jaccard_matches.png", scale=2)
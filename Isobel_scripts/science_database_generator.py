#!/usr/bin/env python3

import random
location_list = ['North East', 'South', 'Midwest', 'West']
dept_list = ['Molecular Biology', 'Chemistry', 'Neuroscience', 'Ecology', 'Bioinformatics']
style_list = ['Wet', 'Dry', 'Both']
interaction_list = ['Lots', 'Some', 'Minimal']
org_list = ['Human', 'Mouse', 'Arabidopsis', 'Fly', 'Worm', 'Yeast', 'Zebrafish', 'Non-Model Organism', 'None']
tech_list = ['Sequencing', 'Microscopy', 'Flow Cytometry', 'Western Blot', 'Coding']

name_list = []
with open('science_database.txt', 'r') as input_file:
    for line in input_file:
        line = line.rstrip()
        name_list.append(line)

data_dict = {}
for name in name_list:
    data_dict[name] = {}
    data_dict[name]['location'] = random.choice(location_list)
    data_dict[name]['department'] = random.choice(dept_list)
    data_dict[name]['style'] = random.choice(style_list)
    data_dict[name]['interaction'] = random.choice(interaction_list)
    data_dict[name]['organism'] = random.choice(org_list)
    data_dict[name]['technique'] = random.choice(tech_list)

output_file = open('science_database.txt', 'w')
for name in data_dict:
    output_file.write(f'{name}\t{data_dict[name]['location']}\t{data_dict[name]['department']}\t{data_dict[name]['style']}\t{data_dict[name]['interaction']}\t{data_dict[name]['organism']}\t{data_dict[name]['technique']}\n')

print('Database generated and written to science_database.txt')
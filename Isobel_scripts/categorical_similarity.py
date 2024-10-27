#!/usr/bin/env python3

import sys

file_input = sys.argv[1]


data_dict = {}
with open(file_input, 'r') as dataset:
    for line in dataset:
        line = line.rstrip()
        [name, color, animal, food]= line.split('\t')
        data_dict[name] = {}
        data_dict[name]['color'] = color
        data_dict[name]['animal'] = animal
        data_dict[name]['food'] = food

user_data = {'color':'red', 'animal':'dog', 'food':'pizza'}
user_set = set(user_data.values())

jaccard_dict = {} #calulating Jaccard distance: (overlap of A and B) / (sum of A and B)
for name in data_dict:
    data_set = set(data_dict[name].values())
    set_overlap = data_set & user_set
    set_sum = data_set | user_set
    jaccard = len(set_overlap) / len(set_sum)
    jaccard_dict[name] = jaccard


gower_dict = {} #calculating Gower similarity: sum of (0 if not match, 1 if match) across variables / # of variables
for name in data_dict:
    gower_sum = 0
    for key in user_data:
        if user_data[key] == data_dict[name][key]: #0.5 if similar but not identical? Would need to define similar things
            gower_sum +=1
    gower = gower_sum / len(user_data)
    gower_dict[name] = gower


write_file = open('categorical_similarity.txt', 'w')
for name in jaccard_dict:
    write_file.write(f'{name}\t{jaccard_dict[name]}\t{gower_dict[name]}\n')

#higher score is more similar for both calculations

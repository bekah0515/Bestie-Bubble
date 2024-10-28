#!/usr/bin/env python3

def similarity_calc():
    data_dict = {}
    with open('science_database.txt', 'r') as dataset:
        for line in dataset:
            line = line.rstrip()
            [name, location, department, style, interaction]= line.split('\t')
            data_dict[name] = {}
            data_dict[name]['location'] = location
            data_dict[name]['department'] = department
            data_dict[name]['style'] = style
            data_dict[name]['interaction'] = interaction

    user_data = {}
    with open('user_science_answers.txt', 'r') as dataset:
        for line in dataset:
            line = line.rstrip()
            [username, location, department, style, interaction] = line.split('\t')
    user_data['location'] = location
    user_data['department'] = department
    user_data['style'] = style
    user_data['interaction'] = interaction
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
    write_file.write(f'{username}\t1\t1\n')
    for name in jaccard_dict:
        write_file.write(f'{name}\t{jaccard_dict[name]}\t{gower_dict[name]}\n')

    #higher score is more similar for both calculations
#!/usr/bin/env python3


def science_quiz():
    username = input('Enter your name:\n')
    print('Where would you like to work?')
    user_dict = {}

    location_list = ['North East', 'South', 'Midwest', 'West']
    location = input(f'Choose one: {location_list}\n').title()
    if location not in location_list:
        print(f'Location not recognized, please choose from the list')
        location = input(f'Choose one: {location_list}\n')
    user_dict['location'] = location


    print('What department are you looking for?')

    dept_list = ['Molecular Biology', 'Chemistry', 'Neuroscience', 'Ecology', 'Bioinformatics']
    department = input(f'Choose one: {dept_list}\n').title()
    if department not in dept_list:
        print(f'Department not recognized, please choose from the list')
        department = input(f'Choose one: {dept_list}\n')
    user_dict['department'] = department

    print('Wet lab, dry lab, or both?')
    style_list = ['Wet', 'Dry', 'Both']
    style = input(f'Choose one: {style_list}\n').title()
    if style not in style_list:
        print(f'Lab style not recognized, please choose from the list')
        style = input(f'Choose one: {style_list}\n').title()
    user_dict['style'] = style

    print('Lots of interaction with your PI, some interaction with your PI, or minimal interaction with your PI?')
    interaction_list = ['Lots', 'Some', 'Minimal']
    interaction = input(f'Choose one: {interaction_list}\n').title()
    if interaction not in interaction_list:
        print(f'Interaction level not recognized, please choose from the list')
        style = input(f'Choose one: {style_list}\n').title()
    user_dict['interaction'] = interaction

    output_file = open('user_science_answers.txt', 'w')
    output_file.write(f'{username}\t')
    for question in user_dict:
        output_file.write(f'{user_dict[question]}\t')
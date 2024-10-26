#!/usr/bin/env python3

import math

def euclidean_distance(dict1, dict2):
    """Calculates the Euclidean distance between two dictionaries.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.

    Returns:
        float: The Euclidean distance between the two dictionaries.
    """

    common_keys = set(dict1.keys()) & set(dict2.keys())
    squared_distance = sum((dict1[key] - dict2[key]) ** 2 for key in common_keys)
    return math.sqrt(squared_distance)

# Example usage
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 2, 'c': 4, 'd': 5}


# distance = euclidean_distance(dict1, dict2)
# print(distance)

#### Output Dictionary. user_eu_dict { USER2: EuDis, USER3: EuDis, USER4: EuDis,... }
### Actually using the function 

def euclidean_distance(dict1, dict2):
    common_keys = set(dict1.keys()) & set(dict2.keys())
    squared_distance = sum((dict1[key] - dict2[key]) ** 2 for key in common_keys)
    return math.sqrt(squared_distance)
userdatabase = { 'Peter' : {'a': 1, 'b': 2, 'c': 3},
'Sarah' : {'a': 5, 'b': 5, 'c': 5},
'Zed' : {'a': 3, 'b': 1, 'c': 1},
'Sally' : {'a': 3, 'b': 1, 'c': 1},
'Matrin' : {'a': 4, 'b': 3, 'c': 1}}
user = 'Sally'

#Weight each value by a multipler - Neutral x1, Not Important x0, Very Important x2, Required x50 
#This would be added to the OG Dictionary --> Weight Dictionary can be fed into this.

user_eu_dict = {}
for otheruser in userdatabase:
    if user != otheruser:
        eudis = euclidean_distance(userdatabase[user], userdatabase[otheruser])
        user_eu_dict[otheruser] = eudis
    else:
        continue
print(user_eu_dict)
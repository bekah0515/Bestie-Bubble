#!/usr/bin/env python3
import pandas as pd
import re
import sys

# I have a CSV file.

# A line looks like this:
# SMOLLY,3,5,3,4,3,3,2,5,1,5,2,3,4,1,3,1,2,1,3,1,1,4,1,5,1,5,3,4,5,3,3,2,5,3,3,1,3,3,5,3,1,2,4,2,3,1,4,2,5,3

# I need to make a Dictionary1 - UserDict.
# I want the KEY to be the first column (i.e. SMOLLY).
# The VALUE is a Dictionary2 - AttDict. 
# There are 5 KEYS in ATTDict. 

# For ATTDict KEY 1 - the VALUES are column 2, 3, 4, 5, 6, 7, 8, 9, 10, and 11.
# For ATTDict KEY 2 - the VALUES are column 12, 13, 14, 15, 16, 17, 18, 19, 20, and 21.
# For ATTDict KEY 3 - the VALUES are column 22, 23, 24, 25, 26, 27, 28, 29, 30, and 31
# For ATTDict KEY 4 - the VALUES are column 32, 33, 34, 35, 36, 37, 38, 39, 40, and 41
# For ATTDict KEY 4 - the VALUES are column 42, 43, 44, 45, 46, 47, 48, 49, 50, and 51.

# Categories are: (A)greeableness, (E)motional (s)tability/neuroticism, (Ex)traversion, (C)onscientiousness, and (O)penness.


import csv

def FileToDict(filename):
    user_dict = {}
    with open(filename, mode='r') as INPUT:
        
        csv_reader = csv.reader(INPUT)
        for row in csv_reader:
            user_name = row[0]
            att_dict = {
                'Agreeableness': row[1:11],
                'Extroverted': row[11:21],
                'Openness': row[21:31],
                'Conscientiousness': row[31:41],
                'Neuroticism': row[41:51]
            }
            user_dict[user_name] = att_dict
            
        return user_dict


# Main execution block
if __name__ == "__main__":
    # Example usage
    import json
    file_path = '../BETA/30subs.named.csv'  
    user_dict = FileToDict(file_path)
    with open('30UserSubbed.txt', 'w') as file:
        json.dump(user_dict, file)



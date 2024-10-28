#!/usr/bin/env python3
import pandas as pd
import re
import sys

# Categories are: (A)greeableness, (E)motional (s)tability/neuroticism, (Ex)traversion, (C)onscientiousness, and (O)penness.
# For the user_dict above, I need to subset it and save the output to a new dictionary - topmatchdict.

# I have a list of top matches. Each index in topmatchlist is a name (ex. 'SMOLLY').
# I want to only include user_dict KEYS that match an index in topmatchlist.

def TopMatchDB(TopMatchList, DataBaseDict):
    TopMatchList = TopMatchList[0]
    topmatchdict = {key: DataBaseDict[key] for key in TopMatchList if key in DataBaseDict}
    return topmatchdict

#I have this dictionary. I want to calculate the distance for each sub-key
# (i.e. Agreeableness, Openness, Neuroticism, Openness, Conscientiousness)
# between the main key (i.e. SMOLLY and BIGGY and save that to a list.

# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    import math
    distance = 0.0
    for i in range(len(row1)):
        distance += (int(row1[i]) - int(row2[i])) ** 2
    return math.sqrt(distance)

# Calculate distances
def EuD4Match(Username, Matchname, data):
    distances = {}
    for trait in data[Username]:
        row1 = data[Username][trait]
        row2 = data[Matchname][trait]
        distances[trait] = euclidean_distance(row1, row2)
    return distances

#Generates Euclidean Distances for Attributes Between User and Top Matches
def EuDict(Username, filename, TPList):     #ADD TOPMATCHLIST ???
    import json 
    #filename = '30subs.named.csv' #SUBJECT TO CHANGE
    with open(filename, 'r') as BigDB:
        data = BigDB.read()
        user_dict = json.loads(data)
    # topmatchlist = TPList
    TopMatchDict = TopMatchDB(TPList, user_dict)
         
    # Loop through topmatchlist to calculate and print Euclidean distances
    EucliDict = {}
    for topmatch in TPList[0]:
        if topmatch != Username:  # Avoid comparing SMOLLY with itself
            EuDisUserVsMatch = EuD4Match(Username, topmatch, TopMatchDict)
            #print(f"Distances between {Username} and {topmatch}: {EuDisUserVsMatch}")
            EucliDict[topmatch] = EuDisUserVsMatch
    return EucliDict

# Main execution block
if __name__ == "__main__":
    filename = '30UserSubbed.txt'
    user = 'SMOLLY'
    topmatchlist = ['SMOLLY', 'Leah Huff', 'Pamela Wheeler', 'Amanda Herrera MD', 'Thomas Powell'] #READ IN???
    EuDisUserVsMatch = EuDict(user, filename, topmatchlist)
    print(EuDisUserVsMatch)
    

# Calling on input DB & Functions Demo: (Worked)
# if __name__ == "__main__":
#     import json 
#     with open('30UserSubbed.txt', 'r') as BigDB:
#         data = BigDB.read()
#         user_dict = json.loads(data)
#     #print(DBDict)
#     topmatchlist = ['SMOLLY', 'Leah Huff', 'Pamela Wheeler', 'Amanda Herrera MD', 'Thomas Powell']
#     SmollyMatches = TopMatchDB(topmatchlist, user_dict)
#     #print(SmollyMatches)
#     EuDisSmollyVBiggy = EuD4Match('SMOLLY', 'Leah Huff', SmollyMatches)
#     #print(EuDisSmollyVBiggy)
#     # Loop through topmatchlist to calculate and print Euclidean distances
#     EucliDict = {}
#     for topmatch in topmatchlist:
#         if topmatch != 'SMOLLY':  # Avoid comparing SMOLLY with itself
#             EuDisUserVsMatch = EuD4Match('SMOLLY', topmatch, SmollyMatches)
#             print(f"Distances between SMOLLY and {topmatch}: {EuDisUserVsMatch}")
#             EucliDict[topmatch] = EuDisUserVsMatch





    # Simlest Example Usage (Worked)
    # data = {
    #     'SMOLLY': {
    #         'Agreeableness': ['3', '5', '3', '4', '3', '3', '2', '5', '1', '5'],
    #         'Extroverted': ['2', '3', '4', '1', '3', '1', '2', '1', '3', '1'],
    #         'Openness': ['1', '4', '1', '5', '1', '5', '3', '4', '5', '3'],
    #         'Conscientiousness': ['3', '2', '5', '3', '3', '1', '3', '3', '5', '3'],
    #         'Neuroticism': ['1', '2', '4', '2', '3', '1', '4', '2', '5', '3']
    #     },
    #     'BIGGY': {
    #         'Agreeableness': ['2', '3', '4', '4', '3', '2', '1', '3', '2', '5'],
    #         'Extroverted': ['4', '4', '4', '2', '2', '2', '2', '2', '1', '3'],
    #         'Openness': ['1', '4', '1', '4', '2', '4', '1', '4', '4', '3'],
    #         'Conscientiousness': ['4', '2', '2', '2', '3', '3', '4', '2', '4', '2'],
    #         'Neuroticism': ['5', '1', '2', '1', '4', '2', '5', '3', '4', '4']
    #     }
    # }
    # Username = 'SMOLLY'
    # Matchname = 'BIGGY'
    # EuDisSmollyVBiggy = EuD4Match(Username, Matchname, data)
    # print(EuDisSmollyVBiggy)
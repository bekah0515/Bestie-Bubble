#!/usr/bin/env python3

import sys
import InputToDict as ITD
from nn_algorithmRK_fixed import nn_algorithm
import InputToDatabase as ITDB
import TopMatchDict as TMD
import DictToScoreToRadar as DTSTR


# Main execution block
if __name__ == "__main__":
    # #Generate Database for K-NN
    # file_path = "30subs.named.csv"
    # user_db = ITDB.FileToDict(file_path)
    # #print(user_db)
    
    #Generate K-NN Matches
    repfile = sys.argv[1]
    inputfile = sys.argv[2]
    #user = 'David Duke'
    user_name, result_dict, list_of_matches = nn_algorithm(repfile, inputfile)
    # print(result_dict)
    # print(list_of_matches)
    user = user_name
    TPList = list_of_matches
    print(f'TopMatchList: {TPList}')

    #Generate "Read-in-able Dictionary"
    import json
    
    file_path = '../BETA/30subs.named.csv'  
    user_dict = ITDB.FileToDict(file_path)
    with open('30UserSubbed.txt', 'w') as file:
        json.dump(user_dict, file)
    #print(user_dict)
    
    #Use Top Matches for EuDisDict
    EuDisUserVsMatch = TMD.EuDict(user, '30UserSubbed.txt', TPList) #KeyError: 'David Duke'
    #print(EuDisUserVsMatch)

    ##Use EuDisDict to Make SpyderPlots
    DTSTR.SpyderScPlot(user, EuDisUserVsMatch)
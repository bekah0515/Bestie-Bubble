#!/usr/bin/env python3

import sys, pandas, os
import InputToDict as ITD
from nn_algorithmRK_fixed import nn_algorithm
import InputToDatabase as ITDB
import TopMatchDict as TMD
import DictToScoreToRadar as DTSTR
import plotly.express as px
from euclid_grapher import euclid_grapher


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
    import pandas as pd
    import sys
    df1 = pd.read_csv(repfile, header=None)
    df2 = pd.read_csv(inputfile, header=None)
    combined_df = pd.concat([df1,df2], axis=0, ignore_index = False)
    combined_df.to_csv("combined_file.csv", header=None, index = False)
    file_path = "combined_file.csv"  
    user_dict = ITDB.FileToDict(file_path)
    with open('30UserSubbed.txt', 'w') as file:
        json.dump(user_dict, file)
    #print(user_dict)
    
    #Use Top Matches for EuDisDict
    EuDisUserVsMatch = TMD.EuDict(user, '30UserSubbed.txt', TPList) #KeyError: 'David Duke'
    #print(EuDisUserVsMatch)

    ##Use EuDisDict to Make SpyderPlots
    DTSTR.SpyderScPlot(user, EuDisUserVsMatch)

    #make 1-d plot of distances
    euclid_grapher(result_dict, user)
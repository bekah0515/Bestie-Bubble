#!/usr/bin/env python3


import InputToDict as ITD
import InputToDatabase as ITDB
import TopMatchDict as TMD
import DictToScoreToRadar as DTSTR
import nn_algorithmRK as NNRK

# Main execution block
if __name__ == "__main__":
    #Generate Database for K-NN
    file_path = "file_path_to_big_csv"
    user_db = ITDB.FileToDict(file_path)
    #print(user_db)
    
    #Generate K-NN Matches
    repfile = user_db
    inputfile = "file_path_to_user_csv"
    user = "grab_name_from_file_name"
    topmatchlist = nn_algorithm(repfile, inputfile)
    #print(topmatchlist)

    #Generate "Read-in-able Dictionary"
    filename = "file_path_to_big_csv"
    user_dict = ITD.FileToDict(filename)
    #print(user_dict)
    
    #Use Top Matches for EuDisDict
    EuDisUserVsMatch = EuDict(user, user_dict)
    #print(EuDisUserVsMatch)

    ##Use EuDisDict to Make SpyderPlots
    SpyderScPlot(user, EuDisUserVsMatch)
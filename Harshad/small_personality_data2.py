#!/Users/pfb2024/mamba/envs/projects/bin/python
import pandas as pd
import re
dict1 = {}
global_dict = {}
with open("personality_data_info.txt", 'r') as input_file:
    lines = input_file.readlines()
    for line in lines:
        key, value = line.strip().split('\t')
        big_key = key[0:3]
        #print(big_key)
        if big_key not in global_dict:
            global_dict[big_key] = {}
        dict1[key.strip()] = value.strip()
        if big_key in global_dict:
            global_dict[big_key][key] = value.strip()
        print(global_dict,"@@##$$")
          
    
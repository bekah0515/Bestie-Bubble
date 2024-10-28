#!/Users/pfb2024/mamba/envs/projects/bin/python
import pandas as pd
dict1 = {}
with open("personality_data_info.txt", 'r') as input_file:
    lines = input_file.readlines()
    for line in lines:
        key, value = line.strip().split('\t')
        dict1[key.strip()] = value.strip()
        print(dict1)
     
    
        

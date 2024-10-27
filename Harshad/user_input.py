#!/Users/pfb2024/mamba/envs/projects/bin/python
import pandas as pd
import re
import sys
import json

def function1():

    dict1 = {}
    global_dict = {}
    output_file = 'output_1.txt'
    with open("personality_data_info.txt", 'r') as input_file, open(output_file,"w") as output:
        print('personality_data_info.txt')
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
            #print(global_dict,"@@##$$")
        #print(f'writing to {output_file}')
        output.write(json.dumps(global_dict))
    return(global_dict)

#test_dict = global_dict[big_key]
#print(test_dict)
def function2(username):
    global_dict = function1()
    user_data = {}
    for category in global_dict:
        user_data[category] = {}
        for key in global_dict[category]:
            user_data[category][key] = []
        #if username in key:
            #user_data[key] = value
    print(f"{username}:")
    #print(json.dumps(user_data))
    print(user_data)
   
def main():
    username = input('Enter your name')
    function2(username)

if __name__=='__main__':
    main()    


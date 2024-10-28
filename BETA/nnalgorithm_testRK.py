#!/Users/pfb2024/mamba/envs/bio/bin/python
import sys
from nn_algorithmRK_fixed import nn_algorithm

repfile = sys.argv[1]
inputfile = sys.argv[2]
user_name, result_dict, list_of_matches = nn_algorithm(repfile, inputfile)
print("UserName:", user_name)
print("list of matches:", list_of_matches)
print("result_dict:", result_dict)
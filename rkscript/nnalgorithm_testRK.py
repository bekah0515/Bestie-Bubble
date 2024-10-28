#!/Users/pfb2024/mamba/envs/bio/bin/python
import sys
from nn_algorithmRK import nn_algorithm

repfile = sys.argv[1]
inputfile = sys.argv[2]
top3matches = nn_algorithm(repfile, inputfile)
print(match_name_list)
print(top3matches)
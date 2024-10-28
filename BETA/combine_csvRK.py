#!/Users/pfb2024/mamba/envs/bio/bin/python3
import pandas as pd
import sys


df1 = pd.read_csv(sys.argv[1], header=None)
df2 = pd.read_csv(sys.argv[2], header=None)

combined_df = pd.concat([df1,df2], axis=0, ignore_index = False)
combined_df.to_csv("combined_file.csv", header=None, index = False)

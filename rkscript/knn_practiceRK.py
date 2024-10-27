#!/Users/pfb2024/mamba/envs/bio/bin/python
import pandas as pd

#read in the data using pandas
df = pd.read_csv('diabetes_data.csv')
#check data has been read in properly
df.head()
#print(df.head())

#check number of rows and columns in dataset
print(df.shape)
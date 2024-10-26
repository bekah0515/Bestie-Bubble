#!/Users/pfb2024/mamba/envs/bio/bin/python

#IMPORT REQUIRED MODULES
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
 
#Load Data
data = load_digits().data
pca = PCA(2)
 
#Transform the data
df = pca.fit_transform(data)
 
df.shape
print(df.shape)

##APPLY KMEANS TO OUR DATA
#Initialize the class object
kmeans = KMeans(n_clusters= 10)

#predict the labels of clusters, which returns the array of cluster labels each datapoint belongs to. 
label = kmeans.fit_predict(df)
 
print(label)

##VISUALIZE DATA
#filter rows of original data for cluster 0
filtered_label0 = df[label == 0]
filtered_label2 = df[label == 2]
filtered_label8 = df[label == 8]

#plotting the results
plt.scatter(filtered_label0[:,0] , filtered_label0[:,1])
plt.scatter(filtered_label2[:,0] , filtered_label2[:,1] , color = 'red')
plt.scatter(filtered_label8[:,0] , filtered_label8[:,1] , color = 'black')

plt.show()
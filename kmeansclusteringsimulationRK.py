#!/Users/pfb2024/mamba/envs/bio/bin/python

#IMPORT REQUIRED MODULES
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

##GENERATE RANDOM DATA AND ASSIGN DATA

#generate random people data to visualize kmeans clustering
np.random.seed(42) #initialize the random number generator

#parameters fo the dataset
num_people = 100
num_features = 6
feature_min = 1
feature_max = 10 #plused 1 because max is exclusive

random_people = np.random.randint(feature_min,feature_max+1,size=(num_people, num_features))
#print(random_people)
data = random_people

##CALCULATE KMEANS
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(data) 
label=kmeans.fit_predict(random_people)
print("Cluster labels for each person:",label)

u_labels = np.unique(label)
for i in u_labels:
    plt.scatter(data[label == i , 0] , data[label == i , 1] , label = i)
#show centroids
#plt.scatter(centroids[:,0] , centroids[:,1] , s = 80, color = 'k')
plt.legend()
plt.show()

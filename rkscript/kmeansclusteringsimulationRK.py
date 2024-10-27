#!/Users/pfb2024/mamba/envs/bio/bin/python

#IMPORT REQUIRED MODULES
import math
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

np.random.seed(42)

# Parameters for the dataset
num_people = 10000 # Number of people you want to generate
num_features = 5 # Number of features per person
feature_min = 1  # Minimum value for each feature
feature_max = 10 # Maximum value for each feature

# Generate random people data
random_people = np.random.randint(feature_min, feature_max + 1, size=(num_people, num_features))
# random_people

# Perform k-means clustering
num_clusters = 32 # Number of clusters
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
label = kmeans.fit_predict(random_people)

# Reduce data to 2D for visualization using PCA
pca = PCA(n_components=2)
data_2d = pca.fit_transform(random_people)

u_labels = np.unique(label)

#plotting the results:

for i in u_labels:
    plt.scatter(data_2d[label == i , 0] , data_2d[label == i , 1] , label = i)
plt.legend()
plt.show()
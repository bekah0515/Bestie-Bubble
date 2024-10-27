#!/Users/pfb2024/mamba/envs/bio/bin/python

import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

#Sample data:make 100 representative points with 5 features each
np.random.seed(42) #initialize the random number generator
representative_points = 1+4*np.random.rand(100, 5)
#print(representative_points)

#Test data for which we want to find the nearest neighbors by making 3 new points with 5 features each
new_points = 1+4*np.random.rand(3, 5)

#Initialize the NearestNeighbors model to find the 10 nearest neighbors
n_neighbors = 10
nearest_neighbors = NearestNeighbors(n_neighbors=n_neighbors, algorithm='auto')

#Fit the model on the representative points
nearest_neighbors.fit(representative_points)

#Find the 10 nearest neighbors for each new point
distances, indices = nearest_neighbors.kneighbors(new_points)

#Output the results
for i, (dists, idxs) in enumerate(zip(distances, indices)):
    print(f"New Point {i+1}:")
    print("Indices of Nearest Neighbors:", idxs)
    print("Distances to Nearest Neighbors:", dists)
    print()


#Reduce dimensions to 2D for visualization using PCA
pca = PCA(n_components=2)
rep_points_2d = pca.fit_transform(representative_points)
new_points_2d = pca.transform(new_points)

#Plot representative points
plt.figure(figsize=(10, 6))
plt.scatter(rep_points_2d[:, 0], rep_points_2d[:, 1], color='black', label='Representative Points', alpha=0.6)

#Plot new points
plt.scatter(new_points_2d[:, 0], new_points_2d[:, 1], color='red', label='New Points', marker='X', s=100)

#Draw lines to the 10 nearest neighbors for each new point
for i, (dists, idxs) in enumerate(zip(distances, indices)):
    for idx in idxs:
        plt.plot([new_points_2d[i, 0], rep_points_2d[idx, 0]],
                 [new_points_2d[i, 1], rep_points_2d[idx, 1]], 'k--', linewidth=0.5)

plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.legend()
plt.title("2D Visualization of New Points and their Nearest Neighbors")
plt.show()